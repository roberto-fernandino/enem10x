class Router:
    def db_for_read(self, model, **hints):
        return "replica"

    def db_for_write(self, model, **hints):
        return "default"

    def allow_relation(self, ob1, ob2, **hints):
        return True
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'