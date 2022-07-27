db = db.getSiblingDB("Library");
db.createCollection("Books");
db.createCollection("Transactions");

db.Books.insertMany([
    {
        'name': 'The Lord of the Rings',
        'category': 'Fantasy',
        'rpd':8.0
    },
    {
        'name': 'The Hobbit',
        'category': 'Fantasy',
        'rpd':7.0
    },
    {
        'name': 'The Catcher in the Rye',
        'category': 'Fiction',
        'rpd':6.0
    },
    {
        'name': 'The Great Gatsby',
        'category': 'Fiction',
        'rpd':5.0
    }
]);

