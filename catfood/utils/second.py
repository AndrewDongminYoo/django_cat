from first import Formula, Brand, os
import json


def insert_formula(data):
    try:
        formulas = Formula.objects.filter(url=data.get("url"))
        if formulas.exists():
            formula = formulas.first()
            brand = formula.brand
            site = data.get("site")
            if not Brand.objects.filter(site=site).exists():
                brand.site = site
                brand.save()
            else:
                brand = Brand.objects.get(site=site)
            formula.brand = brand
            brand.save()
            formula.title = data.get("title")
            formula.image = data.get("image")
            calorie = data.get("calorie")
            if calorie:
                formula.calorie = calorie
            formula.site = data.get("site")
            formula.save()
    except InterruptedError as e:
        print(e)


def upload(name=None):
    data_path = os.path.join(os.curdir, "data")
    files = [x for x in os.listdir(data_path) if x.endswith(".json")]
    print(os.path.realpath(os.curdir))

    for fp in files:
        if name and name != fp:
            pass
        else:
            file_path = os.path.join(data_path, fp)
            with open(file=file_path, mode="r", encoding="utf8") as old:
                obj = json.load(old)
                if type(obj) == list:
                    for data in obj:
                        insert_formula(data)
                elif type(obj) == dict:
                    insert_formula(obj)


if __name__ == '__main__':
    upload()
