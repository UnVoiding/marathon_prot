# -*- coding: utf-8

import csv
import names
import datetime
import random

import date_utils as d_utils
import random_utils as r_utils


def generate_runners(filename):
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([
            'Id',
            'Имя',
            'Фамилия',
            'Возраст участника',
            'Дата рождения',
            'Пол',
            'E-mail',
            'Гражданство',
            'Телефон',
            'Дата регистрации',
            'Второй телефон',
            'Город',
            'Экстренный контакт',
            'Экстренный телефон',
            'Размер футболки',
            'Беговой клуб',
            'Является инвалидом',
            'Является профессиональным спортсменом',
            'Является ребёнком',
            'Является элитным спортсменом',
            'Дата и время регистрации на забег',
            'Название забега',
            'Дистанция',
            'Буква бегового кластера',
            'Номер участника',
            'Результат забега',
        ])

        for i in range(1000):
            dob = r_utils.random_datetime(datetime.datetime(year=1900, month=1, day=1), to_time=datetime.datetime.now())
            age = d_utils.calculate_age(dob)
            name = names.get_first_name()
            surname = names.get_last_name()
            reg_date1 = datetime.datetime.now()
            reg_date1 = reg_date1.replace(month=1, day=1)
            reg_date1 = r_utils.random_datetime(reg_date1, reg_date1.replace(year=reg_date1.year + 1))
            reg_date2 = r_utils.random_datetime(reg_date1, reg_date1.replace(year=reg_date1.year + 1))

            runner = [
                i,
                name,
                surname,
                age,
                dob.strftime('%d.%m.%Y'),
                random.choice(['M', 'F']),
                r_utils.random_email(name, surname),
                r_utils.random_citizenship(),
                r_utils.random_phone(),
                reg_date1.strftime('%d.%m.%Y'),
                r_utils.random_phone(),
                r_utils.random_city(),
                names.get_first_name(),
                random.choice(['L', 'XL', 'M', 'S']),
                r_utils.random_club(),
                reg_date2.strftime('%d.%m.%Y'),
                random.randint(0, 1),
                random.randint(0, 1),
                1 if age < 18 else 0,
                random.randint(0, 1),
                'Абсолют Московский Марафон',
                random.choice(['10 км', '42,2 км Московский Марафон 2018']),
                random.choice(['A', 'B', 'C', 'D', 'E', 'F']),
                random.randint(0, 100000),
                '-'
            ]
            csvwriter.writerow(runner)


def import_runners(filename):
    with open(filename, newline='') as csvfile:
        return list(csv.reader(csvfile, delimiter=';', quotechar='|'))


if __name__ == "__main__":
    data = import_runners('f:\\Work\\Marathon\\марафон проект для посетителей и участников марафона\\registrations_from_runc.run.csv')
    for e in data[1:]:
        print(e)
    # generate_runners('f:\\Work\\Marathon\\марафон проект для посетителей и участников марафона\\sample_runners.csv')