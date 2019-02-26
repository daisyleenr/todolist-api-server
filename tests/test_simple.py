# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from model import *
from config import TEST_DB_STRING

engine = create_engine(TEST_DB_STRING, echo=True, pool_recycle=3600)
Session = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


def create_new_todo(todo_title):
    todo = Todos(title=todo_title)
    db_session.add(todo)
    db_session.commit()
    return todo


def get_todo_list():
    return db_session.query(Todos).all()


def get_todo_by_id(todo_id):
    return db_session.query(Todos).filter_by(id=todo_id).one()


def update_checked(todo, checked):
    todo.checked = checked
    db_session.commit()



class TestSpike:
    def test_one(self):
        assert 1 == 1

    # def test_two(self):
    #     assert 2 == 3

    # def test_compare_string(self):
    #     assert "testint este isentesitnestienwtwi set" == "testint este isenteAAsitnbstienwtwi set"

    def test_new_todo(self):
        todo_1 = create_new_todo('SQLAlchemy 배우기')
        assert todo_1 is not None
        assert todo_1.id is not None

        ret_todo = get_todo_by_id(todo_id=todo_1.id)
        assert ret_todo.title == 'SQLAlchemy 배우기'

    def test_list_todo(self):
        todo_list = get_todo_list()
        assert len(todo_list) > 0
        from pprint import pprint
        pprint(todo_list)

    def test_checked(self):
        todo_1 = create_new_todo('SQLAlchemy 마스터링')
        assert todo_1 is not None
        assert todo_1.id is not None
        assert not todo_1.checked

        todo_1.checked = True
        db_session.add(todo_1)
        db_session.commit()

        assert todo_1.checked

        ret_todo = get_todo_by_id(todo_1.id)
        assert todo_1.title == ret_todo.title
        assert ret_todo.checked

        todo_1.checked = False
        db_session.add(todo_1)
        db_session.commit()

        ret_todo_2 = get_todo_by_id(todo_1.id)
        assert todo_1.title == ret_todo_2.title
        assert not ret_todo_2.checked

    def test_delete(self):
        count_1 = len(db_session.query(Todos).all())
        ret_todo = create_new_todo('삭제 테스트')
        db_session.query(Todos).filter_by(id=ret_todo.id).delete()
        db_session.commit()
        count_2 = len(db_session.query(Todos).all())
        assert count_1 == count_2 # commit이 빠져서 실제로 DB에 반영이 안됬을 때 발견할 수 없음


    # @staticmethod
    # def static_one():
    #     pass
    #
    # @classmethod
    # def class_one(cls):
    #     pass

    # 테스트 전(setup) / 후(teardown) 실행되는 코드
    # exception 발생 확인하는 테스트
    # 시나리오 테스트
    # mock object

    # CRUD 테스트 코드 작성
    # api 코드 변경
