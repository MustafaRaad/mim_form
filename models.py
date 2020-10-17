from django.db import models
import uuid
from django import forms

# ----------نوع طالب التسجيل


class RegisterationType(models.Model):
    REG_TYPE_CHOICES = [
        ('معمل', 'معمل'),
        ('شركة', 'شركة'),
        ('جمعية', 'جمعية'),
        ('تأجير', 'تأجير'),
        ('غير ذلك', 'غير ذلك'),
    ]
    register_type = models.CharField(
        max_length=24, choices=REG_TYPE_CHOICES, verbose_name='نوع طالب التسجيل')
    other = models.CharField(
        max_length=64, blank=True, verbose_name='غير ذلك ان وجد')
    # widget=forms.RadioSelect()

    def __str__(self):
        return self.register_type

    class Meta:
        verbose_name = 'نوع طالب التسجيل'
        verbose_name_plural = 'نوع طالب التسجيل'


# ----------نوع المهنة
class OccupationType(models.Model):
    OCC_TYPE_CHOICES = [
        ('حكومية', 'حكومية'),
        ('مختلطة', 'مختلطة'),
        ('مساهمة', 'مساهمة'),
        ('خاصة', 'خاصة'),
        ('غير ذلك', 'غير ذلك'),
    ]
    occupation_type = models.CharField(
        max_length=24, choices=OCC_TYPE_CHOICES, verbose_name='المهنة')
    other = models.CharField(
        max_length=64, verbose_name='غير ذلك ان وجد', blank=True, )

    def __str__(self):
        return self.occupation_type

    class Meta:
        verbose_name = 'نوع المهنة'
        verbose_name_plural = 'نوع المهنة'


# -----------عناوين المسجل


class RegisterAddresses(models.Model):
    country = models.CharField(max_length=16, verbose_name='الدولة')
    postal = models.IntegerField(
        blank=True, null=True, verbose_name='صندوق البريد')
    phone_number1 = models.CharField(unique=True,
                                     max_length=16, verbose_name='هاتف اول')
    phone_number2 = models.CharField(
        max_length=16, unique=True, null=True, blank=True, verbose_name='هاتف ثاني')
    fax = models.IntegerField(unique=True,
                              blank=True, null=True, verbose_name='فاكس')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    detaild_address_AR = models.TextField(
        verbose_name='العنوان التفصيلي بالعربية')
    detaild_address_EN = models.TextField(
        verbose_name='العنوان التفصيلي بالانكليزية', blank=True)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'عنوان المسجل'
        verbose_name_plural = 'عناوين المسجل'

# ---------نوع الشركة


class CompanyType(models.Model):
    CO_TYPE_CHOICES = [
        ('حكومية', 'حكومية'),
        ('مختلطة', 'مختلطة'),
        ('مساهمة', 'مساهمة'),
        ('خاصة', 'خاصة'),
        ('غير ذلك', 'غير ذلك'),
    ]
    company_type = models.CharField(
        max_length=24, choices=CO_TYPE_CHOICES, verbose_name='نوع الشركة او الهيئة')
    other = models.CharField(
        max_length=64, blank=True,  verbose_name='غير ذلك ان وجد')
    manager_name = models.CharField(
        max_length=64, verbose_name='اسم مالكها / المدير المفوض')

    def __str__(self):
        return self.company_type

    class Meta:
        verbose_name = 'نوع الشركة'
        verbose_name_plural = 'نوع الشركة'

# ------------صفة الوكيل


class ProxyDesc(models.Model):
    PROXY_TYPE_CHOICES = [
        ('محامي', 'محامي'),
        ('مدير مفوض شركة الملكية الفكرية', 'مدير مفوض شركة الملكية الفكرية'),
    ]
    proxy_type = models.CharField(
        max_length=46, choices=PROXY_TYPE_CHOICES, verbose_name='صفة الوكيل')
    lawer_union_no = models.CharField(
        max_length=16, null=True, blank=True, verbose_name='الرقم النقابي')
    ceo_company_no = models.CharField(
        max_length=16, null=True, blank=True, verbose_name='رقم تسجيل الشركة')

    def __str__(self):
        return self.proxy_type

    class Meta:
        verbose_name = 'صفة الوكيل'
        verbose_name_plural = 'صفة الوكيل'
# -----------حق اسبقية العلامة


class PrecedenceRight(models.Model):
    country_of_claim = models.CharField(
        max_length=64, blank=True, null=True, verbose_name='بلد الادعاء ')
    claim_number = models.CharField(
        max_length=64, blank=True, null=True, verbose_name='رقم الادعاء')
    claim_date = models.CharField(
        max_length=64, blank=True, null=True, verbose_name='تأريخ الادعاء')
    proxy_name = models.CharField(
        max_length=64, blank=True, null=True, verbose_name='اسم الوكيل')
    proxy_desc = models.ForeignKey(
        ProxyDesc, verbose_name="صفة الوكيل", on_delete=models.CASCADE)

    def __str__(self):
        return self.claim_number

    class Meta:
        verbose_name = 'حق اسبقية العلامة'
        verbose_name_plural = 'حق اسبقية العلامة'

# ----------الايصال المالي


class Invoice(models.Model):
    invoice_no = models.IntegerField(verbose_name='رقم الايصال المالي')
    invoice_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='تأريخ الايصال المالي')
    paid_fees = models.CharField(
        max_length=50, verbose_name='الرسوم المدفوعة')

    def __str__(self):
        return self.invoice_no

    class Meta:
        verbose_name = 'الايصال المالي'
        verbose_name_plural = 'الايصالات المالية'


# ---------------عنوان الوكيل / شركة الملكية الفكرية

class ProxyAddress(models.Model):
    agency_date_From = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='تاريخ بداية الوكالة')
    agency_date_to = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='تاريخ انتهاء الوكالة')
    postal = models.IntegerField(
        blank=True, null=True, verbose_name='صندوق البريد')
    phone_number1 = models.CharField(
        unique=True, max_length=16, verbose_name='هاتف اول')
    phone_number2 = models.CharField(
        max_length=16, unique=True, null=True, blank=True, verbose_name='هاتف ثاني')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    fax = models.IntegerField(unique=True,
                              blank=True, null=True, verbose_name='فاكس')
    detaild_address = models.TextField(verbose_name='العنوان التفصيلي')
    invoice_no = models.ForeignKey(
        Invoice, verbose_name="رقم الايصال المالي", on_delete=models.CASCADE)

    def __str__(self):
        return self.agency_date_From

    class Meta:
        verbose_name = 'عنوان الوكيل / شركة الملكية الفكرية'
        verbose_name_plural = 'عنوان الوكيل / شركة الملكية الفكرية'


# -----------------قائمة الوثائق الواجب تقديمها مع الطلب
class Documents(models.Model):
    td_logo = models.BooleanField(
        verbose_name="عشرة / نسخ من صورة العلامة التجارية")
    precedence_doc = models.BooleanField(
        verbose_name="صورة عن مستند يثبت حق الاسبقية(ان وجد)")
    agency_doc = models.BooleanField(
        verbose_name="الوكالة (مصدقة حسب الاصول) محفوظة في الاظبارة المرقمة")
    agency_doc_no = models.CharField(
        max_length=64, verbose_name="رقم الاظبارة")

    def __str__(self):
        return self.agency_doc_no

    class Meta:
        verbose_name = 'الوثيقة الواجب تقديمها مع الطلب'
        verbose_name_plural = 'قائمة الوثائق الواجب تقديمها مع الطلب'

# --------------التواقيع


class Signatureinfo(models.Model):
    applicants_name = models.CharField(
        max_length=256, verbose_name='اسم مقدم الطلب (طالب التسجيل/الوكيل)')
    applicants_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='(مقدم الطلب) تأريخ تقديم الطلب')
    applicants_sign = models.ImageField(
        upload_to='Signatures/applicants', verbose_name='توقيع مقدم الطلب')

    inforamtion_officer_name = models.CharField(
        max_length=256, verbose_name='اسم موظف المعلومات')
    information_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='(موظف المعلومات) تأريخ تقديم الطلب')
    inforamtion_officer_sign = models.ImageField(
        upload_to='Signatures/inforamtion_officer', verbose_name='توقيع موظف المعلومات')

    computer_officer_name = models.CharField(
        max_length=256, verbose_name='اسم موظف الحاسبة')
    computer_date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='(موظف الحاسبة) تأريخ تقديم الطلب')
    computer_officer_sign = models.ImageField(
        upload_to='Signatures/computer_officer', verbose_name='توقيع موظف الحاسبة')

    def __str__(self):
        return self.applicants_name

    class Meta:
        verbose_name = 'توقيع تقديم الطلب'
        verbose_name_plural = 'تواقيع تقديم الطلب'

# ------------------وصف العلامة


class LogoDesc(models.Model):
    # applicants_name = models.ForeignKey(
    #     Signatureinfo, verbose_name='اسم مقدم الطلب', on_delete=models.CASCADE, related_name='applicants_name')
    logo = models.ImageField(
        upload_to='Logos', max_length=None, verbose_name='صورة العلامة')
    names = models.CharField(
        max_length=256, verbose_name='اسماء', blank=True, )
    symbols = models.CharField(
        max_length=256, verbose_name='حروف و رموز', blank=True)
    numbers = models.CharField(
        max_length=256, verbose_name='ارقام', blank=True)
    Geometric_form = models.CharField(
        max_length=256, verbose_name='اشكال هندسية', blank=True)
    Color = models.CharField(max_length=256, verbose_name='الوان', blank=True)
    other = models.CharField(
        max_length=256, verbose_name='غير ذلك', blank=True)
    desc_ar = models.TextField(
        verbose_name='المعنى باللغة العربية', blank=True)
    CO_TYPE_CHOICES = [
        ('تجارية', 'تجارية'),
        ('خدمة', 'خدمة'),
        ('ضمان', 'ضمان'),
        ('جماعية', 'جماعية'),
        ('مشهورة', 'مشهورة'),
        ('غير ذلك', 'غير ذلك'),
    ]
    company_type = models.CharField(
        max_length=24, choices=CO_TYPE_CHOICES, verbose_name='نوع الشركة او الهيئة')
    conditions = models.TextField(blank=True,
                                  verbose_name='اية شروط او قيود يرغب طالب التسجيل تحديدها لتسجيل العلامة')

    def __str__(self):
        return self.applicants_name

    class Meta:
        verbose_name = 'وصف العلامة'
        verbose_name_plural = 'وصف العلامة'

# --------------- الاصناف المطلوبة تسجيل العلامة فيها


class LogoClass(models.Model):
    class_number = models.IntegerField(verbose_name='رقم الصنف')
    material_code = models.CharField(max_length=256, verbose_name='رمز المادة')
    good_or_service = models.CharField(
        max_length=256, verbose_name='البضاعة او الخدمة')

    def __str__(self):
        return self.class_number

    class Meta:
        verbose_name = 'الاصناف المطلوبة تسجيل العلامة فيها'
        verbose_name_plural = 'الاصناف المطلوبة تسجيل العلامة فيها'


# ------------معلومات المسجل
class RegisterInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='تاريخ تسجيل الاستمارة')
    name_ar = models.CharField(
        max_length=256, unique=True, verbose_name='الاسم بالعربي')
    name_en = models.CharField(
        max_length=256, unique=True, verbose_name='الاسم بالانكليزي')


# ----------نوع طالب التسجيل
    register_type = models.ForeignKey(
        RegisterationType, on_delete=models.CASCADE, null=True, verbose_name='نوع طالب التسجيل')

# ----------نوع المهنة
    occupation_type = models.ForeignKey(
        OccupationType, on_delete=models.CASCADE, null=True, verbose_name='نوع المهنة')

# -----------عناوين المسجل
    register_addresses = models.ForeignKey(
        RegisterAddresses, on_delete=models.CASCADE, null=True, verbose_name='عناوين المسجل')

# ---------نوع الشركة
    co_type = models.ForeignKey(
        CompanyType, on_delete=models.CASCADE, null=True, verbose_name='نوع الشركة')

# ------------صفة الوكيل
    proxy_desc = models.ForeignKey(
        ProxyDesc, on_delete=models.CASCADE, null=True, verbose_name='صفة الوكيل')

# -----------حق اسبقية العلامة
    precedence_right = models.ForeignKey(
        PrecedenceRight, on_delete=models.CASCADE, null=True, verbose_name='حق اسبقية العلامة')

# ----------الايصال المالي
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, null=True, verbose_name='الايصال المالي')

# ---------------عنوان الوكيل / شركة الملكية الفكرية
    Proxy_address = models.ForeignKey(
        ProxyAddress, on_delete=models.CASCADE, null=True, verbose_name='عنوان الوكيل / شركة الملكية الفكرية')


# -----------------قائمة الوثائق الواجب تقديمها مع الطلب
    documents = models.ForeignKey(Documents, on_delete=models.CASCADE,
                                  null=True, verbose_name='قائمة الوثائق الواجب تقديمها مع الطلب')

# --------------التواقيع
    signature_info = models.ForeignKey(
        Signatureinfo, on_delete=models.CASCADE, null=True, verbose_name='التواقيع')

# ------------------وصف العلامة
    logo_desc = models.ForeignKey(
        LogoDesc, on_delete=models.CASCADE, null=True, verbose_name='وصف العلامة')

# --------------- الاصناف المطلوبة تسجيل العلامة فيها
    logo_class = models.ForeignKey(
        LogoClass, on_delete=models.CASCADE, null=True, verbose_name='الاصناف المطلوبة تسجيل العلامة فيها')

    def __str__(self):
        return self.name_ar

    class Meta:
        verbose_name = 'استمارة التسجيل'
        verbose_name_plural = 'استمارات التسجيل'
