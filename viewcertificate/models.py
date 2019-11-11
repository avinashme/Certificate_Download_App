from django.db import models


class Application(models.Model):
    application_id = models.AutoField(db_column='APPLICATION_ID', primary_key=True)  # Field name made lowercase.
    application_name = models.CharField(db_column='APPLICATION_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APPLICATION'


class Athletes(models.Model):
    athletes_id = models.AutoField(db_column='ATHLETES_ID', primary_key=True)  # Field name made lowercase.
    bibno = models.CharField(db_column='BIBNO', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='SURNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='COUNTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    race = models.ForeignKey('Racedetails', models.DO_NOTHING, db_column='RACE_ID')  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DATEOFBIRTH', blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='AGE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MOBILENUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='Category_ID')  # Field name made lowercase.
    subcategoryid = models.IntegerField(db_column='SUBCATEGORYID', blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATHLETES'


class Category(models.Model):
    category_id = models.AutoField(db_column='Category_ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    associatedcategory_id = models.IntegerField(db_column='AssociatedCategory_ID', blank=True, null=True)  # Field name made lowercase.
    race_id = models.IntegerField(db_column='RACE_ID')  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORY'


class Custompermissions(models.Model):
    permissions_id = models.AutoField(db_column='PERMISSIONS_ID', primary_key=True)  # Field name made lowercase.
    section = models.CharField(db_column='SECTION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    showhide = models.BooleanField(db_column='SHOWHIDE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMPERMISSIONS'


class Location(models.Model):
    location_id = models.AutoField(db_column='Location_ID', primary_key=True)  # Field name made lowercase.
    location_start = models.CharField(db_column='Location_Start', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location_end = models.CharField(db_column='Location_End', max_length=50, blank=True, null=True)  # Field name made lowercase.
    race = models.ForeignKey('Racedetails', models.DO_NOTHING, db_column='RACE_ID')  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    editedon = models.CharField(db_column='EditedOn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    editedby = models.DateTimeField(db_column='EditedBy', blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION'


class Livedashboard(models.Model):
    livedashboard_id = models.AutoField(db_column='LIVEDASHBOARD_ID', primary_key=True)  # Field name made lowercase.
    bibno = models.CharField(db_column='BIBNO', max_length=50)  # Field name made lowercase.
    athletename = models.CharField(db_column='ATHLETENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pointarrivaltime = models.DateTimeField(db_column='POINTARRIVALTIME', blank=True, null=True)  # Field name made lowercase.
    race = models.ForeignKey('Racedetails', models.DO_NOTHING, db_column='RACE_ID')  # Field name made lowercase.
    readerno = models.CharField(db_column='READERNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='Category_ID')  # Field name made lowercase.
    subcategoryid = models.IntegerField(db_column='SUBCATEGORYID', blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.
    recordno = models.IntegerField(db_column='RecordNo', blank=True, null=True)  # Field name made lowercase.
    splitpos = models.CharField(db_column='SPLITPOS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LiveDashboard'


class Racedetails(models.Model):
    race_id = models.AutoField(db_column='RACE_ID', primary_key=True)  # Field name made lowercase.
    race_name = models.CharField(db_column='RACE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    race_organizer = models.CharField(db_column='RACE_ORGANIZER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    race_guntime = models.DateTimeField(db_column='RACE_GUNTIME', blank=True, null=True)  # Field name made lowercase.
    totallaps = models.IntegerField(db_column='TotalLaps', blank=True, null=True)  # Field name made lowercase.
    racetype = models.CharField(db_column='RACETYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totaldistance = models.DecimalField(db_column='TOTALDISTANCE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.
    associatedrace = models.IntegerField(db_column='AssociatedRace', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RACEDETAILS'


class Reader(models.Model):
    reader_id = models.AutoField(db_column='READER_ID', primary_key=True)  # Field name made lowercase.
    race_id = models.IntegerField(db_column='RACE_ID')  # Field name made lowercase.
    readerno = models.CharField(db_column='READERNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    readerip = models.CharField(db_column='READERIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER'


class Readerconfig(models.Model):
    readerconfig_id = models.AutoField(db_column='READERCONFIG_ID', primary_key=True)  # Field name made lowercase.
    race = models.ForeignKey(Racedetails, models.DO_NOTHING, db_column='RACE_ID')  # Field name made lowercase.
    positionid = models.IntegerField(db_column='POSITIONID')  # Field name made lowercase.
    readerno = models.CharField(db_column='READERNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    splitpos = models.CharField(db_column='SPLITPOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    minreachtime = models.CharField(db_column='MINREACHTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    totaldistance = models.DecimalField(db_column='TotalDistance', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READERCONFIG'


class Results(models.Model):
    results_id = models.AutoField(db_column='RESULTS_ID', primary_key=True)  # Field name made lowercase.
    bibno = models.CharField(db_column='BIBNO', max_length=50)  # Field name made lowercase.
    race_id = models.IntegerField(db_column='RACE_ID')  # Field name made lowercase.
    race_name = models.CharField(db_column='RACE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    race_organizer = models.CharField(db_column='RACE_ORGANIZER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    athletename = models.CharField(db_column='ATHLETENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    race_guntime = models.CharField(db_column='RACE_GUNTIME', max_length=50)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='Category_ID')  # Field name made lowercase.
    category_name = models.CharField(db_column='Category_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    associatedcategory_id = models.IntegerField(db_column='AssociatedCategory_ID', blank=True, null=True)  # Field name made lowercase.
    associatedcategory_name = models.CharField(db_column='AssociatedCategory_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    associatedgender = models.CharField(db_column='AssociatedGender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='STARTTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='ENDTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nettime = models.CharField(db_column='NETTIME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    racestatus = models.TextField(db_column='RaceStatus', blank=True, null=True)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MobileNumber', max_length=10)  # Field name made lowercase.
    totaldistance = models.DecimalField(db_column='TOTALDISTANCE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    grosstime = models.CharField(db_column='GrossTime', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avgspeed = models.FloatField(db_column='AvgSpeed', blank=True, null=True)  # Field name made lowercase.
    isdatavalid = models.IntegerField(db_column='IsDataValid', blank=True, null=True)  # Field name made lowercase.
    overallpace = models.CharField(db_column='OVERALLPACE', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTS'


class Temporarybibdetails(models.Model):
    tbd_id = models.AutoField(db_column='TBD_ID', primary_key=True)  # Field name made lowercase.
    bibno = models.CharField(db_column='BIBNO', max_length=50)  # Field name made lowercase.
    race = models.ForeignKey(Racedetails, models.DO_NOTHING, db_column='RACE_ID')  # Field name made lowercase.
    pointarrivaltime = models.DateTimeField(db_column='POINTARRIVALTIME', blank=True, null=True)  # Field name made lowercase.
    isrecordprocessed = models.BooleanField(db_column='IsRecordProcessed')  # Field name made lowercase.
    isuploaded = models.BooleanField(db_column='IsUploaded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TemporaryBIBDetails'


class Userpermissions(models.Model):
    userpermission_id = models.AutoField(db_column='USERPERMISSION_ID', primary_key=True)  # Field name made lowercase.
    permissions_id = models.IntegerField(db_column='PERMISSIONS_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERPERMISSIONS'


class Userrole(models.Model):
    role_id = models.AutoField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERROLE'


class Userrolebase(models.Model):
    rolebase_id = models.AutoField(db_column='ROLEBASE_ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    section = models.CharField(db_column='SECTION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERROLEBASE'


class Users(models.Model):
    user_id = models.AutoField(db_column='USER_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=100)  # Field name made lowercase.
    user_password = models.CharField(db_column='USER_PASSWORD', max_length=100)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS'
