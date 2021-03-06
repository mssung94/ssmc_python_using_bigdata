from flask import Flask,request,session,redirect,url_for
from flask_ex.service.model import initDBHelper, DBManager

def create_app(config_path = './resource/config.cfg'):
    app = Flask(__name__)
    # 각종 설정 삽입될것
    app.secret_key = 'slakdfjlkasdfjlkasdfj' # session 생성을 위해
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 1. 환경변수 설정
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    initConfig(app,config_path)
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 2. DB 설정
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #    
    initDBHelper(app) # Pooling
    DBManager.init(app) # ORM
    DBManager.init_db()

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 3. Error 설정
    #   - 각종 오류 코드 발생시 일괄처리
    #   - Not Found 같은걸 커스터마이징 하고 싶다면
    #   - 위키피디아 가서 HTTP 응답코드 확인해보자  
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    initErrorPage(app)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 4. 라우트 설정( 블루프린트 )
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    initBlueprint(app)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 5. LifeCycle 처리 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    initReqRes(app)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    return app

# 1. 환경변수 설정
def initConfig(app,config_path):
    #   - 프로그램에서 사용되는 고정된 정보
    #   - 디비접속정보, 운영상 필요한 상수값 등
    #   - class로부터(객체),리소스(파일),운영체제로부터 가져올 수 있다
    #   - 코드에 하드코딩되어있지 않고, 환경변수를 읽어서 프로그램에 반영시키는 방식 => 관리나 유지보수가 좋다     
    app.config.from_pyfile( config_path, silent=True ) # cfg 파일을 읽기 위해

    # class를 읽어서 객체로부터 환경변수를 획득 
    # -> 직관성, 코드에 적용되어 있음
    # 내 위치가 하위에 있다고 하더라도 from을 기술할때는 풀경로를 기술 
    from flask_ex.service.config import DBConfig # 시작은 start.py이니까
    app.config.from_object( DBConfig )

    # 로그된 환경변수값 확인
    # configCheck(app.config.items())
    # TEST_URL에 해당된는 값을 출력하시오
    # 환경변수의 값은 그 의도대로 타입을 따라간다 
    print(app.config['DB_PORT'])
    # print(app.config.get('TEST_URL'))
    # print(app.config.get('SERVER_RUN_MODE_IS_REAL'))

# 2. DB 설정
# model에서 구현할 예정

# 3. Error 설정
def initErrorPage(app):
    from flask_ex.service.error import not_found # ㄹㅇ 모듈 땡기기는 어디서든 가능하구나
    app.register_error_handler(404,not_found) # 404라는 누가 처리할건지 함수도 적어줘야함

# 4. 라우트 설정( 블루프린트 )
def initBlueprint(app):
    #   - blueprint => 주제별로 페이지를 나눠서 개발가능 => controller
    #       - 회원관리 : ~/users/login, ~/users/logout, ~/users/signup
    from flask_ex.service.controller import bp_users,bp_analysis
    #       - 분석관리 : ~/analysis/init, ~/analysis/proc, ~/analysis/sum    
    from flask_ex.service.controller import user,ana # 해당 모듈이 통째로 메모리에 올라온다 -> 객체가 만들어지듯이 사용에 관계없음
    # blueprint를 Flask 객체에 등록
    # http://127.0.0.1:3000/users/login 로 접속해야함
    app.register_blueprint(bp_users, url_prefix='/users')
    app.register_blueprint(bp_analysis, url_prefix='/analysis')

# 5. LifeCycle 처리
def initReqRes(app):
    #   - 브라우저에서 주소치고 엔터쳐서 화면이 보이기까지 사이클
    #   - 어떤  페이지던 하나의 경로를 거쳐서 개별 페이지로 가고
    #   - 응답도 동일, 이곳에서 필터를 구현하여 요청을 걸러버린다
    
    @app.before_first_request
    def before_first_request():
        print('서버가 가동하고 최초 요청시 단 한번 반응함')
    
    # 모든 요청이 들어오는 곳 => 세션 처리를 해야함
    @app.before_request
    def before_request(): pass
        # 모든 요청이 들어오는 곳 -> 여기서 우린 세션 처리를 해야함
        # print('모든 요청이 들어오는 곳',request.url)
        
        # # 세션검사를 해서
        # # 세션이 없으면
        # if not 'user_id' in session:
        #     # 요청페이지가 /users/login이 아닌 경우에만 포워딩 -> 아니라면 음수값 리턴하기 때문에
        #     if request.url.find(url_for('users_bp.login')) < 0:
        #         # ~/users/login로 이동하고
        #         return redirect(url_for('users_bp.login')) # 블루프린트.함수명 으로 해야 다른 함수랑 겹치치 않음
        # # 세션이 있으면 
        #     # -> 없으면 그냥 무시 

    # 모든 응답이 지나가는 곳, 공통 작업이 있을 경우 처리
    @app.after_request
    def after_request(res):
        print('매 요청이 처리되고 나서 응답이 지나가는 곳')
        return res

    # 
    @app.teardown_request
    def teardown_request(exception):
        print('브라우저가 응답하고 실행')
        return '브라우저가 응답하고 실행'

    #
    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print('http요청(app context)이 완전히 종료되고 호출')

def configCheck(items):
    # print(items)
    # 환경변수 키, 환경변수 값 출력 <- dict 형태니까
    for key,value in items:
        print(key,value)