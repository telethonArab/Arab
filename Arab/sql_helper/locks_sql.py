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

iqvois1 = "Arab/helpers/styles/Voic/ابو عباس لو تاكل خره.ogg"
iqvois2 = "Arab/helpers/styles/Voic/استمر نحن معك.ogg"
iqvois3 = "Arab/helpers/styles/Voic/افحط بوجه.ogg"
iqvois4 = "Arab/helpers/styles/Voic/اكعد لا اسطرك سطره العباس.ogg"
iqvois5 = "Arab/helpers/styles/Voic/اللهم لا شماته.ogg"
iqvois6 = "Arab/helpers/styles/Voic/امرع دينه.ogg"
iqvois7 = "Arab/helpers/styles/Voic/امشي بربوك.ogg"
iqvois8 = "Arab/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
iqvois9 = "Arab/helpers/styles/Voic/انت سايق زربه.ogg"
iqvois10 = "Arab/helpers/styles/Voic/اوني تشان.ogg"
iqvois11 = "Arab/helpers/styles/Voic/برافو عليك استادي.ogg"
iqvois12 = "Arab/helpers/styles/Voic/بلوك محترم.ogg"
iqvois13 = "Arab/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
iqvois14 = "Arab/helpers/styles/Voic/بيتش.ogg"
iqvois15 = "Arab/helpers/styles/Voic/تخوني ؟.ogg"
iqvois15 = "Arab/helpers/styles/Voic/تره متكدرلي.ogg"
iqvois17 = "Arab/helpers/styles/Voic/تعبان اوي.ogg"
iqvois18 = "Arab/helpers/styles/Voic/تكذب.ogg"
iqvois19 = "Arab/helpers/styles/Voic/حسبي الله.ogg"
iqvois20 = "Arab/helpers/styles/Voic/حشاش.ogg"
iqvois21 = "Arab/helpers/styles/Voic/حقير.ogg"
iqvois22 = "Arab/helpers/styles/Voic/خاص.ogg"
iqvois23 = "Arab/helpers/styles/Voic/خاله ما تنامون.ogg"
iqvois24 = "Arab/helpers/styles/Voic/خرب شرفي اذا ابقى بالعراق.ogg"
iqvois25 = "Arab/helpers/styles/Voic/دكات الوكت الاغبر.ogg"
iqvois26 = "Arab/helpers/styles/Voic/ررردح.ogg"
iqvois27 = "Arab/helpers/styles/Voic/سلامن عليكم.ogg"
iqvois28 = "Arab/helpers/styles/Voic/شعليك.ogg"
iqvois29 = "Arab/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
iqvois30 = "Arab/helpers/styles/Voic/شلون ،.ogg"
iqvois31 = "Arab/helpers/styles/Voic/صح لنوم.ogg"
iqvois32 = "Arab/helpers/styles/Voic/صمت.ogg"
iqvois33 = "Arab/helpers/styles/Voic/ضحكة مصطفى الحجي.ogg"
iqvois34 = "Arab/helpers/styles/Voic/طماطه.ogg"
iqvois35 = "Arab/helpers/styles/Voic/طيح الله حضك.ogg"
iqvois36 = "Arab/helpers/styles/Voic/فاك يوو.ogg"
iqvois37 = "Arab/helpers/styles/Voic/فرحان.ogg"
iqvois38 = "Arab/helpers/styles/Voic/لا تضل تضرط.ogg"
iqvois39 = "Arab/helpers/styles/Voic/لا تقتل المتعه يا مسلم.ogg"
iqvois40 = "Arab/helpers/styles/Voic/لا مستحيل.ogg"
iqvois41 = "Arab/helpers/styles/Voic/لا والله شو عصبي.ogg"
iqvois42 = "Arab/helpers/styles/Voic/لش.ogg"
iqvois43 = "Arab/helpers/styles/Voic/لك اني شعليه.ogg"
iqvois44 = "Arab/helpers/styles/Voic/ما اشرب.ogg"
iqvois45 = "Arab/helpers/styles/Voic/مع الاسف.ogg"
iqvois46 = "Arab/helpers/styles/Voic/مقتدى.ogg"
iqvois47 = "Arab/helpers/styles/Voic/من رخصتكم.ogg"
iqvois48 = "Arab/helpers/styles/Voic/منو انت.ogg"
iqvois49 = "Arab/helpers/styles/Voic/منورني.ogg"
iqvois50 = "Arab/helpers/styles/Voic/نتلاكه بالدور الثاني.ogg"
iqvois51 = "Arab/helpers/styles/Voic/نستودعكم الله.ogg"
iqvois52 = "Arab/helpers/styles/Voic/ها شنهي.ogg"
iqvois53 = "Arab/helpers/styles/Voic/ههاي الافكار حطها.ogg"
iqvois54 = "Arab/helpers/styles/Voic/وينهم.ogg"
iqvois55 = "Arab/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois56 = "Arab/helpers/styles/Voic/اريد انام.ogg"
iqvois57 = "Arab/helpers/styles/Voic/افتحك فتح.ogg"
iqvois58 = "Arab/helpers/styles/Voic/اكل خره لدوخني.ogg"
iqvois59 = "Arab/helpers/styles/Voic/السيد شنهو السيد.ogg"
iqvois60 = "Arab/helpers/styles/Voic/زيج2.ogg"
iqvois61 = "Arab/helpers/styles/Voic/زيج لهارون.ogg"
iqvois62 = "Arab/helpers/styles/Voic/زيج الناصرية.ogg"
iqvois63 = "Arab/helpers/styles/Voic/راقبو اطفالكم.ogg"
iqvois64 = "Arab/helpers/styles/Voic/راح اموتن.ogg"
iqvois65 = "Arab/helpers/styles/Voic/ذس اس مضرطة.ogg"
iqvois66 = "Arab/helpers/styles/Voic/دروح سرسح منا.ogg"
iqvois67 = "Arab/helpers/styles/Voic/خويه ما دكوم بيه.ogg"
iqvois68 = "Arab/helpers/styles/Voic/خلصت تمسلت ديلة كافي انجب.ogg"
iqvois69 = "Arab/helpers/styles/Voic/بعدك تخاف.ogg"
iqvois70 = "Arab/helpers/styles/Voic/بسبوس.ogg"
iqvois71 = "Arab/helpers/styles/Voic/اني بتيتة كحبة.ogg"
iqvois72 = "Arab/helpers/styles/Voic/انعل ابوكم لابو اليلعب وياكم طوبة.ogg"
iqvois73 = "Arab/helpers/styles/Voic/انت شدخلك.ogg"
iqvois74 = "Arab/helpers/styles/Voic/انا ماشي بطلع.ogg"
iqvois75 = "Arab/helpers/styles/Voic/امداك وامده الخلفتك.ogg"
iqvois76 = "Arab/helpers/styles/Voic/امبيههههه.ogg"
iqvois77 = "Arab/helpers/styles/Voic/هدي بيبي.ogg"
iqvois78 = "Arab/helpers/styles/Voic/هاه صدك تحجي.ogg"
iqvois79 = "Arab/helpers/styles/Voic/مو كتلك رجعني.ogg"
iqvois80 = "Arab/helpers/styles/Voic/مامرجية منك هاية.ogg"
iqvois81 = "Arab/helpers/styles/Voic/ليش هيجي.ogg"
iqvois82 = "Arab/helpers/styles/Voic/كـــافـي.ogg"
iqvois83 = "Arab/helpers/styles/Voic/كس اخت السيد.ogg"
iqvois84 = "Arab/helpers/styles/Voic/شنو كواد ولك اني هنا.ogg"
iqvois85 = "Arab/helpers/styles/Voic/شجلبت.ogg"
iqvois86 = "Arab/helpers/styles/Voic/شبيك وجه الدبس.ogg"
iqvois87 = "Arab/helpers/styles/Voic/سييييي.ogg"
iqvois88 = "Arab/helpers/styles/Voic/زيجج1.ogg"
iqvois89 = "Arab/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois90 = "Arab/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
iqvois91 = "Arab/helpers/styles/Voic/وينهم.ogg"
iqvois92 = "Arab/helpers/styles/Voic/هيلو سامر وحود.ogg"
iqvois93 = "Arab/helpers/styles/Voic/هو.ogg"
iqvois94 = "Arab/helpers/styles/Voic/ههاي الافكار حطها.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
