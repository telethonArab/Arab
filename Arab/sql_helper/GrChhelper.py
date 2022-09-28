from sqlalchemy import Column, String, delete
from sqlalchemy.orm.exc import NoResultFound
from . import BASE, SESSION
class GrChiq(BASE):
    __tablename__ = "AutoGrChiqthon"
    AutoGr = Column(String, primary_key=True)
    def __init__(self, AutoGr):
        self.AutoGr = str(AutoGr)
GrChiq.__table__.create(checkfirst=True)
def Auto_ChGR(AutoGr):
    try:
        if SESSION.query(GrChiq).one():
            deletAutoChGR()
    except NoResultFound:
        pass
    user = GrChiq(AutoGr)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True
def deletAutoChGR():   
    to_check = getGrChAuto()
    if not to_check:
        return False
    stmt = delete(GrChiq)
    SESSION.execute(stmt)
    SESSION.commit()
    return stmt
def getGrChAuto():
    try:
        if _result := SESSION.query(GrChiq).one().AutoGr:
            return _result
    except NoResultFound:
        return None
    finally:
        SESSION.close()

# iqthon
