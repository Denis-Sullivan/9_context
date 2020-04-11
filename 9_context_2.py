import datetime


class MyOpen():

  def __init__(self, file_path):
    self.file_path = file_path
    self.time_start = datetime.datetime.now()

  def __enter__(self):
    self.file = open(self.file_path)
    return self.file

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.file.close()
    self.time_stop = datetime.datetime.now()
    print('Время запуска кода:    ', self.time_start)
    print('Время окончания работы:', self.time_stop)
    print('На выполнение кода было потрачено: {0} сек.'.format(self.time_stop - self.time_start))


def horoscope():
  month = input('Введите месяц: ')
  month = month.lower()
  date = int(input('Введите число: '))


  if (month in {'январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь'} and 1 <= date <= 31) or (month in {'апрель', 'июнь', 'сентябрь', 'ноябрь'} and 1 <= date <= 30) or (month == 'февраль' and 1 <= date <= 28):
    if (date >= 22 and month == 'декабрь') or (date <= 20  and month == 'январь'):
      print('Козерог')
    elif (date >= 21 and month == 'январь') or (date <= 19  and month == 'февраль'):
      print('Водолей')
    elif (date >= 20 and month == 'февраль') or (date <= 20 and month == 'март'):
      print('Рыбы')
    elif (date >= 21 and month == 'март') or (date <= 20  and month == 'апрель'):
      print('Овен')
    elif (date >= 21 and month == 'апрель') or (date <= 21  and month == 'май'):
      print('Телец')
    elif (date >= 22 and month == 'май') or (date <= 21 and month == 'июнь'):
      print('Близнецы')
    elif (date >= 22 and month == 'июнь') or (date <= 22  and month == 'июль'):
      print('Рак')
    elif (date >= 23 and month == 'июль') or (date <= 22  and month == 'август'):
      print('Лев')
    elif (date >= 23 and month == 'август') or (date <= 22  and month == 'сентябрь'):
      print('Дева')
    elif (date >= 23 and month == 'сентябрь') or (date <= 22  and month == 'октябрь'):
      print('Весы')
    elif (date >= 23 and month == 'октябрь') or (date <= 22  and month == 'ноябрь'):
      print('Скорпион')
    elif (date >= 23 and month == 'ноябрь') or (date <= 21  and month == 'декабрь'):
      print('Стрелец')
  elif month == 'февраль' and date == 29:
    year = int(input('Год вашего рождения? (например 1988): '))
    if year % 4 == 0:
      print('Очень редкая дата рождения - по знаку вы Рыбы')
    else:
      print('Это не високосный год, попробуйте еще раз')
  else:
    print('вы ввели неверные данные, попробуйте еще раз')

if __name__ == '__main__':
  with MyOpen('test.txt') as f:
    horoscope()
