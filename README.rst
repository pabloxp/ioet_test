Example IOET Test Python Developer
==============================

What Is This?
-------------

This is a simple Python application intended to provide a working example to
calculate payroll from txt files.
The goal of these to show python skills.

How To Use This
---------------

python3 main.py --payrule [payrule file location] --payroll [payroll file location]

Where payrule is a txt file with pay rates by hour and day and payroll
is a txt file with employees shifts

Example:
python3 main.py --payrule tests/testpayrule.txt --payroll tests/testpayroll.txt

Payrule example:
MO00:01-09:00-25
MO09:01-18:00-15
MO18:01-00:00-20

First 2 character are the day, second 5 characters are the shift starting hour,
the third 5 characters are the shift ending hour and the last 2 character is the
USD value per hour.

Payroll example:
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

The first characters are the name, then the working hours separated by comma
