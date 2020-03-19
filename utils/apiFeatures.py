class ApiFeature:
    def __init__(self, query, queryObj, model):
        self.query = query
        self.queryObj = dict(queryObj)
        self.model = model
        
    
    def filter(self):
        queryObj2 = dict()
        excluedField = ['page', 'sort', 'limit', 'fields']
        for key, value in self.queryObj.items():
            if key not in excluedField:
                queryObj2[key] = value
        for key, value in queryObj2.items():
            if hasattr(self.model, key):
                self.query = self.query.filter(getattr(self.model, key) == value)
        return self
        
    def sort(self):
        if self.queryObj.get('sort'):
            sortBy = self.queryObj['sort'].split(',')
            for i in sortBy:
                if hasattr(self.model,i) or hasattr(self.model, i[1::]):
                    if i[0] == '-':
                        order_by = getattr(self.model, i[1::]).desc()
                    else:
                        order_by = getattr(self.model, i)
                    self.query = self.query.order_by(order_by)
        else:
            self.query = self.query.order_by(self.model.createdAt.desc())
        return self
    
    def paginate(self):
        page = int(self.queryObj.get('page', 1))
        limit = int(self.queryObj.get('limit', 2))
        skip = (page-1)*limit
        self.query = self.query.limit(limit).offset(skip)
        return self
        