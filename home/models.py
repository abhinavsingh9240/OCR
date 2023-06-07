from django.contrib.auth.models import User
from django.db import models

# Create your models here.
LANGUAGE_CHOICES = (
    # ("eng","English"),
    # ("hin","Hindi"),
    (None,"None"),
    ("afr", "Afrikaans"), ("amh", "Amharic"), ("ara", "Arabic"), ("asm", "Assamese"), ("aze", "Azerbaijani"),
    ("aze_cyrl", "Azerbaijani - Cyrilic"), ("bel", "Belarusian"), ("ben", "Bengali"), ("bod", "Tibetan"),
    ("bos", "Bosnian"), ("bre", "Breton"), ("bul", "Bulgarian"), ("cat", "Catalan"), ("ceb", "Cebuano"),
    ("ces", "Czech"), ("chi_sim", "Chinese - Simplified"), ("chi_sim_vert", "Chinese - Simplified - Vertical"),
    ("chi_tra", "Chinese - Traditional"), ("chr", "Cherokee"), ("cos", "Corsican"), ("cym", "Welsh"),
    ("dan", "Danish"), ("dan_frak", "Danish - Fraktur"), ("deu", "German"),("deu_frak", "German - Fraktur"), ("dzo", "Dzongkha"),
    ("ell", "Greek, Modern"), ("eng", "English"), ("enm", "English, Middle"), ("epo", "Esperanto"), ("equ", "Math / equation"),
    ("est", "Estonian"), ("eus", "Basque"), ("fao", "Faroese"), ("fas", "Persian"), ("fil", "Filipino (old - Tagalog)"),

    ("fin", "Finnish"), ("fra", "French"), ("frk", "German - Fraktur"), ("frm", "French, Middle"), ("fry", "Western Frisian	"),
    ("gla", "Scottish Gaelic"), ("gle", "Irish"), ("glg", "Galician"), ("grc", "Greek, Ancient"),
    ("guj", "Gujarati"), ("hat", "Haitian"), ("heb", "Hebrew"), ("hin", "Hindi"), ("hrv", "Croatian"),
    ("hun", "Hungarian"), ("hye", "Armenian"), ("iku", "Inuktitut"),
    ("ind", "Indonesian"), ("isl", "Icelandic"), ("ita", "Italian"), ("ita_old", "Italian - Old"),

    ("jav", "Javanese"), ("jpn", "Japanese"), ("jpn_vert", "Japanese - Vertical"), ("kan", "Kannada"), ("kat", "Georgian"),
    ("kat_old", "Georgian - Old"), ("kaz", "Kazakh"), ("khm", "Central Khmer"), ("kir", "Kirghiz, Kyrgyz"),
    ("kmr", "Kurmanji"), ("kor", "Korean"), ("kor_vert", "Korean (vertical)"), ("lao", "Lao"), ("lat", "Latin"),
    ("lav", "Latvian"), ("lit", "Lithuanian"), ("ltz", "Luxembourgish"),
    ("mal", "Malayalam"), ("mar", "Marathi"), ("mkd", "Macedonian"), ("mlt", "Maltese"),

    ("mon", "Mongolian"), ("mri", "Maori"), ("msa", "Malay"), ("mya", "Burmese"), ("nep", "Nepali"),
    ("nld", "Dutch; Flemish"), ("nor", "Norwegian"), ("oci", "Occitan"), ("ori", "Oriya"),
    ("pan", "Punjabi"), ("pol", "Polish"), ("por", "Portuguese"), ("pus", "Pushto"), ("que", "Quechua"),
    ("ron", "Romanian"), ("rus", "Russian"), ("san", "Sanskrit"),
    ("sin", "Sinhala"), ("slk", "Slovak"), ("slv", "Slovenian"), ("snd", "Sindhi"),

    ("spa", "Spanish"), ("sqi", "Albanian"), ("srp", "Serbian"), ("srp_latn", "Serbian - Latin"), ("sun", "Sundanese"),
    ("swa", "Swahili"), ("swe", "Swedish"), ("syr", "Syriac"), ("tam", "Tamil"),
    ("tat", "Tatar"), ("tel", "Telugu"), ("tgk", "Tajik"), ("tgl", "Tagalog (new - Filipino)"), ("tha", "Thai"),
    ("tir", "Tigrinya"), ("ton", "Tonga"), ("tur", "Turkish"),
    ("uig", "Uighur"), ("ukr", "Ukrainian"), ("urd", "Urdu"), ("uzb", "Uzbek"),
    ("uzb_cyrl", "Uzbek - Cyrilic"), ("vie", "Vietnamese"), ("yid", "Yiddish"), ("yor", "Yoruba")
)


class Data(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    primary_lang = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default='hin'
    )
    secondary_lang = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default= None,
        null=True,
        blank=True,
    )
