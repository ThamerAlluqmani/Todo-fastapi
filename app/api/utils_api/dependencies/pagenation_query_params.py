from fastapi import Query


class PaginationQueryParams:
    def __init__(self, offset: int = Query(0, ge=0), limit: int = Query(2, le=100, gt=0)):
        self.offset = offset
        self.limit = limit
