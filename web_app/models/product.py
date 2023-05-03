
DEFAULT_PRODUCTS = [
    # see: https://picsum.photos/images
    {'id': 1, 'name': 'Unsweetened Cold Brew $10', 'description': '25 oz Original cold brew coffee, unsweetened', 'price': 10, 'url': 'https://raw.githubusercontent.com/carolinacpe95/cafecito-brews-images/main/Botellas.jpg'},
    {'id': 2, 'name': 'Sweetened Cold Brew $11', 'description': '25 oz Monkfruit sweetened cold brew', 'price': 11, 'url': 'https://raw.githubusercontent.com/carolinacpe95/cafecito-brews-images/main/Coffee.jpg'},
    {'id': 3, 'name': 'Carajillo Six Pack $12', 'description': '6 Carajillos to-go. Combination of cold brew and Licor 43 (21+)', 'price': 12, 'url': 'https://github.com/carolinacpe95/cafecito-brews-images/blob/main/Screen%20Shot%202023-05-02%20at%2012.24.28%20PM.png?raw=true'},
    {'id': 4, 'name': 'Paower Shot Six Pack $15', 'description': '6 Individual Cold Brew bottles to go, unsweetened', 'price': 15, 'url': 'https://raw.githubusercontent.com/carolinacpe95/cafecito-brews-images/main/Screen%20Shot%202023-05-02%20at%2012.23.46%20PM.png'},
    {'id': 5, 'name': 'Paower Bites $8', 'description': '6 Dark Chocolate, Almond Butter, Cold Brew Infused Bites', 'price': 8, 'url': 'https://raw.githubusercontent.com/carolinacpe95/cafecito-brews-images/main/Screen%20Shot%202023-05-02%20at%2012.20.47%20PM.png'},
    {'id': 6, 'name': 'Cold Brew Ice Cream $8', 'description': '16 oz Pint of Cold Brew Vanilla Ice Cream', 'price': 8, 'url': 'https://raw.githubusercontent.com/carolinacpe95/cafecito-brews-images/main/IceCream.jpg'},
]


class Product:
    def __init__(self, attrs):
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.description = attrs.get("description")
        self.price = attrs.get("price")
        self.url = attrs.get("url")
        self.created_at = attrs.get("created_at")

    @property
    def to_row(self):
        return [self.id, self.name, self.description, self.price, self.url, str(self.created_at)]
