# Generated by Django 4.2.11 on 2024-04-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_delete_class_remove_aircraft_seat_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manfact',
            name='name',
            field=models.CharField(choices=[('Airbus', 'Airbus'), ('Boeing', 'Boeing'), ('Bombardier', 'Bombardier'), ('Embraer', 'Embraer'), ('Lockheed Martin', 'Lockheed Martin'), ('Textron Aviation', 'Textron Aviation'), ('Mitsubishi Aircraft Corporation', 'Mitsubishi Aircraft Corporation'), ('Antonov', 'Antonov'), ('Saab', 'Saab'), ('Dassault Aviation', 'Dassault Aviation'), ('Tupolev', 'Tupolev'), ('Ilyushin', 'Ilyushin'), ('Aerospatiale', 'Aerospatiale'), ('British Aerospace', 'British Aerospace'), ('Fokker', 'Fokker'), ('McDonnell Douglas', 'McDonnell Douglas'), ('ATR', 'ATR'), ('Pilatus Aircraft', 'Pilatus Aircraft'), ('Cessna', 'Cessna'), ('Gulfstream Aerospace', 'Gulfstream Aerospace'), ('Piaggio Aerospace', 'Piaggio Aerospace'), ('Honda Aircraft Company', 'Honda Aircraft Company'), ('Diamond Aircraft Industries', 'Diamond Aircraft Industries'), ('Cirrus Aircraft', 'Cirrus Aircraft'), ('Emivest Aerospace', 'Emivest Aerospace'), ('Leonardo S.p.A.', 'Leonardo S.p.A.'), ('Kawasaki Heavy Industries', 'Kawasaki Heavy Industries'), ('Tecnam', 'Tecnam'), ('Beechcraft', 'Beechcraft'), ('Piper Aircraft', 'Piper Aircraft'), ('AgustaWestland', 'AgustaWestland'), ('Israel Aerospace Industries', 'Israel Aerospace Industries'), ('Groen Brothers Aviation', 'Groen Brothers Aviation'), ('PZL Świdnik', 'PZL Świdnik'), ('Kamov', 'Kamov'), ('Beriev', 'Beriev'), ('Harbin Aircraft Industry Group', 'Harbin Aircraft Industry Group'), ('Xi’an Aircraft Industrial Corporation', 'Xi’an Aircraft Industrial Corporation'), ('Shanghai Aircraft Manufacturing Factory', 'Shanghai Aircraft Manufacturing Factory'), ('Xi’an Aircraft Company', 'Xi’an Aircraft Company'), ('Shaanxi Aircraft Corporation', 'Shaanxi Aircraft Corporation'), ('Harbin Aircraft Manufacturing Corporation', 'Harbin Aircraft Manufacturing Corporation'), ('Shenyang Aircraft Corporation', 'Shenyang Aircraft Corporation'), ('Nanchang Aircraft Manufacturing Corporation', 'Nanchang Aircraft Manufacturing Corporation'), ('Jiangxi Hongdu Aviation Industry', 'Jiangxi Hongdu Aviation Industry'), ('Xian Aircraft Design Institute', 'Xian Aircraft Design Institute'), ('Nanchang Aircraft Company', 'Nanchang Aircraft Company'), ('Shanghai Aviation Industrial Company', 'Shanghai Aviation Industrial Company'), ('China Aviation Industry Corporation I', 'China Aviation Industry Corporation I'), ('China Aviation Industry Corporation II', 'China Aviation Industry Corporation II'), ('AVIC Aircraft', 'AVIC Aircraft'), ('AVIC General Aircraft', 'AVIC General Aircraft'), ('Chengdu Aircraft Industry Group', 'Chengdu Aircraft Industry Group'), ('AVIC Harbin Aircraft Industry Group', 'AVIC Harbin Aircraft Industry Group'), ('AVIC Helicopter', 'AVIC Helicopter'), ('AVIC Xi’an Aircraft Industry (Group) Company', 'AVIC Xi’an Aircraft Industry (Group) Company'), ('AVIC Xi’an Aircraft Industry Company Limited', 'AVIC Xi’an Aircraft Industry Company Limited'), ('AVIC Xian Aircraft Corporation', 'AVIC Xian Aircraft Corporation'), ('AVIC Nanchang Aircraft Corporation', 'AVIC Nanchang Aircraft Corporation'), ('AVIC Guizhou Aircraft Corporation', 'AVIC Guizhou Aircraft Corporation'), ('AVIC Harbin Aircraft Industry (Group) Company', 'AVIC Harbin Aircraft Industry (Group) Company'), ('AVIC Hongdu Aviation Industry Group', 'AVIC Hongdu Aviation Industry Group'), ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'), ('AVIC Harbin Dongan Engine Manufacturing Company', 'AVIC Harbin Dongan Engine Manufacturing Company'), ('AVIC Aviation Engine Corporation', 'AVIC Aviation Engine Corporation'), ('AVIC Aero-Engine Controls Company', 'AVIC Aero-Engine Controls Company'), ('AVIC Flight Automatic Control Research Institute', 'AVIC Flight Automatic Control Research Institute'), ('AVIC Harbin Dongan Aero Engine Group', 'AVIC Harbin Dongan Aero Engine Group'), ('AVIC Harbin Aircraft Industry (Group) Co., Ltd.', 'AVIC Harbin Aircraft Industry (Group) Co., Ltd.'), ('AVIC Harbin Aviation Industry Group', 'AVIC Harbin Aviation Industry Group'), ('AVIC Aviation Industry Corporation of China', 'AVIC Aviation Industry Corporation of China'), ('AVIC Aircraft Co., Ltd.', 'AVIC Aircraft Co., Ltd.'), ('AVIC Changhe Aircraft Industries Corporation', 'AVIC Changhe Aircraft Industries Corporation'), ('AVIC Hafei Aviation Industry Company', 'AVIC Hafei Aviation Industry Company'), ('AVIC Commercial Aircraft Engine Company', 'AVIC Commercial Aircraft Engine Company'), ('AVIC Changhe Aviation Industry Corporation', 'AVIC Changhe Aviation Industry Corporation'), ('AVIC Harbin Aircraft Industry Group Company', 'AVIC Harbin Aircraft Industry Group Company'), ('AVIC Harbin Aircraft Corporation', 'AVIC Harbin Aircraft Corporation'), ('AVIC Harbin Turbine Engine Company', 'AVIC Harbin Turbine Engine Company'), ('AVIC Hanzhong Aircraft Industry Company', 'AVIC Hanzhong Aircraft Industry Company'), ('AVIC Nanchang Aircraft Manufacturing Corporation', 'AVIC Nanchang Aircraft Manufacturing Corporation'), ('AVIC Chengdu Aircraft Corporation', 'AVIC Chengdu Aircraft Corporation'), ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'), ('AVIC Harbin Aircraft Manufacturing Corporation', 'AVIC Harbin Aircraft Manufacturing Corporation'), ('AVIC Changhe Aircraft Corporation', 'AVIC Changhe Aircraft Corporation'), ('AVIC Shaanxi Aircraft Corporation', 'AVIC Shaanxi Aircraft Corporation'), ('AVIC Chengdu Aircraft Industrial (Group) Company', 'AVIC Chengdu Aircraft Industrial (Group) Company'), ('AVIC Nanchang Aircraft Manufacturing Corporation', 'AVIC Nanchang Aircraft Manufacturing Corporation'), ('AVIC Nanchang Aircraft Corporation', 'AVIC Nanchang Aircraft Corporation'), ('AVIC Shenyang Aircraft Corporation', 'AVIC Shenyang Aircraft Corporation'), ('AVIC Xi’an Aircraft Industrial Corporation', 'AVIC Xi’an Aircraft Industrial Corporation'), ('AVIC Harbin Aircraft Industrial (Group) Company', 'AVIC Harbin Aircraft Industrial (Group) Company')], max_length=100, unique=True),
        ),
    ]
