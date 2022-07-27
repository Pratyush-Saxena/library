from email.policy import default
from unicodedata import category
from marshmallow import Schema, fields


class BookSchema(Schema):
    name = fields.Str()
    category = fields.Str()
    rpd = fields.Float()


class BookReqSchema(Schema):
    keyword = fields.Str(default="")
    category = fields.Str(default="")
    rpd_range = fields.Str(description="input range of price ex- 100-200", default="")


class BookRespSchema(Schema):
    resp = fields.List(fields.Nested(BookSchema))


class DefaultRespSchema(Schema):
    resp = fields.Str(required=True)

class DefaultReqSchema(Schema):
    input = fields.Str(required=True)

class DefaultRespListSchema(Schema):
    resp = fields.List(fields.Str())
    

class BookIssueSchema(Schema):
    issue_date = fields.Date()
    book = fields.Str()
    user = fields.Str()


class BookReturnSchema(Schema):
    return_date = fields.Date()
    book = fields.Str()
    user = fields.Str()

class ReadersListSchema(Schema):
    resp = fields.Dict()

class BooksIssuedWithinDateSchema(Schema):
    from_date=fields.Date()
    to_date=fields.Date()