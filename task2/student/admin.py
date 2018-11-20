from django.contrib import admin
from .models import Institute,Branch, Fee, Student, Transaction, FeeType

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field

# Register your models here.

# admin.site.register(Branch)
# admin.site.register(Fee)
# admin.site.register(FeeType)
admin.site.register(Student)


class UserResource(resources.ModelResource):
    enrol_no = Field(attribute='student.enrol_no',column_name='enrol_no')
    contact = Field(attribute='student.contact', column_name='contact')
    institute = Field(attribute='student.institute', column_name='institute')
    branch = Field(attribute='student.branch', column_name='branch')
    course = Field(attribute='student.course', column_name='course')
    birth_date = Field(attribute='student.birth_date', column_name='birth_date')

    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name', 'email', 'is_staff',
                  'is_active', 'enrol_no','contact', 'institute', 'branch', 'course', 'birth_date')
        export_order = ('id','username', 'password', 'first_name', 'last_name', 'email', 'is_staff',
                  'is_active', 'enrol_no','contact', 'institute', 'branch', 'course', 'birth_date')


    def dehydrate_enrol_no(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.enrol_no)

    def dehydrate_contact(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.contact)

    def dehydrate_institute(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.institute)

    def dehydrate_branch(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.branch)

    def dehydrate_course(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.course)

    def dehydrate_birth_date(self, user):
        s1 = Student.objects.filter(user=user)
        if s1:
            return '%s' % (user.student.birth_date)

    def hydrate_birth_date(self, user, row):
        print("=====hydrate_enrol_no===", user)
        import pdb
        pdb.set_trace()
        institute = Institute.objects.filter(name=row.get('institute'))
        if institute:
            institute = institute[0]
        branch = Branch.objects.filter(name=row.get('branch'))
        if branch:
            branch = branch[0]
        # course = Branch.objects.filter(name=row.get('course'))


        Student.objects.create(user=user,birth_date=row.get('birth_date'),
            branch=branch, institute=institute, enrol_no= row.get('enrol_no'),
            contact= row.get('contact'), course=row.get('course'))
        

    def import_field(self, field, obj, data):
        print("import_field",field)
        meth = getattr(self, 'hydrate_{}'.format(field.column_name), None)
        if meth is not None:
            print("==if==")
            # store custom field format back into a database
            data = meth(obj, data)
        elif field.attribute and field.column_name in data:
            print("==elif==")
            field.save(obj, data)


    # def after_save_instance(self, instance, dry_run, abc):
    #     print("=====after_save_instance===")
    #     import pdb
    #     pdb.set_trace()
    #     if not dry_run:
    #         for field_name in [self.get_field_name(f) for f in self.get_fields()]:
    #             method = getattr(self, 'hydrate_%s' % field_name, None)
    #             if method is not None:
    #                 print("=====inside if ======")
    #                 method(instance)

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'
    fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    inlines = (StudentInline, )
    list_display = ('username', 'email', 'first_name','last_name', 'is_active')
    search_fields = ['username','email', 'first_name','last_name']
    list_filter = ('is_active', 'is_staff' )


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url_slug', 'email','is_active')
    search_fields = ['name','url_slug']
    list_filter = ('name', 'url_slug')

admin.site.register(Institute,InstituteAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','institute', 'url_slug', 'email','is_active')
    search_fields = ['name', 'institute', 'url_slug', 'state']
    list_filter = ('name', 'url_slug', 'institute', 'state')

admin.site.register(Branch,BranchAdmin)

class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount','is_active')
    search_fields = ['name', 'amount']
    list_filter = ('name', 'is_active')

admin.site.register(FeeType,FeeTypeAdmin)

class FeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_id', 'is_active')
    search_fields = ['user', 'payment_id',]
    list_filter = ('user', 'is_active')

admin.site.register(Fee,FeeAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'paid_amt', 'status', 'payment_id')
    search_fields = ['uuid' ,'user', 'payment_id', 'status']
    list_filter = ('user', 'status')

admin.site.register(Transaction,TransactionAdmin)

