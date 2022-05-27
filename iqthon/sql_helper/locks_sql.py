from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr









def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

iqvois1 = "iqthon/helpers/styles/Voic/ابو عباس لو تاكل خره.ogg"
iqvois2 = "iqthon/helpers/styles/Voic/استمر نحن معك.ogg"
iqvois3 = "iqthon/helpers/styles/Voic/افحط بوجه.ogg"
iqvois4 = "iqthon/helpers/styles/Voic/اكعد لا اسطرك سطره العباس.ogg"
iqvois5 = "iqthon/helpers/styles/Voic/اللهم لا شماته.ogg"
iqvois6 = "iqthon/helpers/styles/Voic/امرع دينه.ogg"
iqvois7 = "iqthon/helpers/styles/Voic/امشي بربوك.ogg"
iqvois8 = "iqthon/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
iqvois9 = "iqthon/helpers/styles/Voic/انت سايق زربه.ogg"
iqvois10 = "iqthon/helpers/styles/Voic/اوني تشان.ogg"
iqvois11 = "iqthon/helpers/styles/Voic/برافو عليك استادي.ogg"
iqvois12 = "iqthon/helpers/styles/Voic/بلوك محترم.ogg"
iqvois13 = "iqthon/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
iqvois14 = "iqthon/helpers/styles/Voic/بيتش.ogg"
iqvois15 = "iqthon/helpers/styles/Voic/تخوني ؟.ogg"
iqvois15 = "iqthon/helpers/styles/Voic/تره متكدرلي.ogg"
iqvois17 = "iqthon/helpers/styles/Voic/تعبان اوي.ogg"
iqvois18 = "iqthon/helpers/styles/Voic/تكذب.ogg"
iqvois19 = "iqthon/helpers/styles/Voic/حسبي الله.ogg"
iqvois20 = "iqthon/helpers/styles/Voic/حشاش.ogg"
iqvois21 = "iqthon/helpers/styles/Voic/حقير.ogg"
iqvois22 = "iqthon/helpers/styles/Voic/خاص.ogg"
iqvois23 = "iqthon/helpers/styles/Voic/خاله ما تنامون.ogg"
iqvois24 = "iqthon/helpers/styles/Voic/خرب شرفي اذا ابقى بالعراق.ogg"
iqvois25 = "iqthon/helpers/styles/Voic/دكات الوكت الاغبر.ogg"
iqvois26 = "iqthon/helpers/styles/Voic/ررردح.ogg"
iqvois27 = "iqthon/helpers/styles/Voic/سلامن عليكم.ogg"
iqvois28 = "iqthon/helpers/styles/Voic/شعليك.ogg"
iqvois29 = "iqthon/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
iqvois30 = "iqthon/helpers/styles/Voic/شلون ،.ogg"
iqvois31 = "iqthon/helpers/styles/Voic/صح لنوم.ogg"
iqvois32 = "iqthon/helpers/styles/Voic/صمت.ogg"
iqvois33 = "iqthon/helpers/styles/Voic/ضحكة مصطفى الحجي.ogg"
iqvois34 = "iqthon/helpers/styles/Voic/طماطه.ogg"
iqvois35 = "iqthon/helpers/styles/Voic/طيح الله حضك.ogg"
iqvois36 = "iqthon/helpers/styles/Voic/فاك يوو.ogg"
iqvois37 = "iqthon/helpers/styles/Voic/فرحان.ogg"
iqvois38 = "iqthon/helpers/styles/Voic/لا تضل تضرط.ogg"
iqvois39 = "iqthon/helpers/styles/Voic/لا تقتل المتعه يا مسلم.ogg"
iqvois40 = "iqthon/helpers/styles/Voic/لا مستحيل.ogg"
iqvois41 = "iqthon/helpers/styles/Voic/لا والله شو عصبي.ogg"
iqvois42 = "iqthon/helpers/styles/Voic/لش.ogg"
iqvois43 = "iqthon/helpers/styles/Voic/لك اني شعليه.ogg"
iqvois44 = "iqthon/helpers/styles/Voic/ما اشرب.ogg"
iqvois45 = "iqthon/helpers/styles/Voic/مع الاسف.ogg"
iqvois46 = "iqthon/helpers/styles/Voic/مقتدى.ogg"
iqvois47 = "iqthon/helpers/styles/Voic/من رخصتكم.ogg"
iqvois48 = "iqthon/helpers/styles/Voic/منو انت.ogg"
iqvois49 = "iqthon/helpers/styles/Voic/منورني.ogg"
iqvois50 = "iqthon/helpers/styles/Voic/نتلاكه بالدور الثاني.ogg"
iqvois51 = "iqthon/helpers/styles/Voic/نستودعكم الله.ogg"
iqvois52 = "iqthon/helpers/styles/Voic/ها شنهي.ogg"
iqvois53 = "iqthon/helpers/styles/Voic/ههاي الافكار حطها.ogg"
iqvois54 = "iqthon/helpers/styles/Voic/وينهم.ogg"
iqvois55 = "iqthon/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois56 = "iqthon/helpers/styles/Voic/اريد انام.ogg"
iqvois57 = "iqthon/helpers/styles/Voic/افتحك فتح.ogg"
iqvois58 = "iqthon/helpers/styles/Voic/اكل خره لدوخني.ogg"
iqvois59 = "iqthon/helpers/styles/Voic/السيد شنهو السيد.ogg"
iqvois60 = "iqthon/helpers/styles/Voic/زيج2.ogg"
iqvois61 = "iqthon/helpers/styles/Voic/زيج لهارون.ogg"
iqvois62 = "iqthon/helpers/styles/Voic/زيج الناصرية.ogg"
iqvois63 = "iqthon/helpers/styles/Voic/راقبو اطفالكم.ogg"
iqvois64 = "iqthon/helpers/styles/Voic/راح اموتن.ogg"
iqvois65 = "iqthon/helpers/styles/Voic/ذس اس مضرطة.ogg"
iqvois66 = "iqthon/helpers/styles/Voic/دروح سرسح منا.ogg"
iqvois67 = "iqthon/helpers/styles/Voic/خويه ما دكوم بيه.ogg"
iqvois68 = "iqthon/helpers/styles/Voic/خلصت تمسلت ديلة كافي انجب.ogg"
iqvois69 = "iqthon/helpers/styles/Voic/بعدك تخاف.ogg"
iqvois70 = "iqthon/helpers/styles/Voic/بسبوس.ogg"
iqvois71 = "iqthon/helpers/styles/Voic/اني بتيتة كحبة.ogg"
iqvois72 = "iqthon/helpers/styles/Voic/انعل ابوكم لابو اليلعب وياكم طوبة.ogg"
iqvois73 = "iqthon/helpers/styles/Voic/انت شدخلك.ogg"
iqvois74 = "iqthon/helpers/styles/Voic/انا ماشي بطلع.ogg"
iqvois75 = "iqthon/helpers/styles/Voic/امداك وامده الخلفتك.ogg"
iqvois76 = "iqthon/helpers/styles/Voic/امبيههههه.ogg"
iqvois77 = "iqthon/helpers/styles/Voic/هدي بيبي.ogg"
iqvois78 = "iqthon/helpers/styles/Voic/هاه صدك تحجي.ogg"
iqvois79 = "iqthon/helpers/styles/Voic/مو كتلك رجعني.ogg"
iqvois80 = "iqthon/helpers/styles/Voic/مامرجية منك هاية.ogg"
iqvois81 = "iqthon/helpers/styles/Voic/ليش هيجي.ogg"
iqvois82 = "iqthon/helpers/styles/Voic/كـــافـي.ogg"
iqvois83 = "iqthon/helpers/styles/Voic/كس اخت السيد.ogg"
iqvois84 = "iqthon/helpers/styles/Voic/شنو كواد ولك اني هنا.ogg"
iqvois85 = "iqthon/helpers/styles/Voic/شجلبت.ogg"
iqvois86 = "iqthon/helpers/styles/Voic/شبيك وجه الدبس.ogg"
iqvois87 = "iqthon/helpers/styles/Voic/سييييي.ogg"
iqvois88 = "iqthon/helpers/styles/Voic/زيجج1.ogg"
iqvois89 = "iqthon/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois90 = "iqthon/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
iqvois91 = "iqthon/helpers/styles/Voic/وينهم.ogg"
iqvois92 = "iqthon/helpers/styles/Voic/هيلو سامر وحود.ogg"
iqvois93 = "iqthon/helpers/styles/Voic/هو.ogg"
iqvois94 = "iqthon/helpers/styles/Voic/ههاي الافكار حطها.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
