from Backend.app.database.models import PositionModel


class PositionRepository:
    def __init__(self, db):
        self.db = db

    def get_position_by_id(self, position_id):
        return self.db.query(PositionModel).filter(PositionModel.id == position_id).first()

    def create_position(self, position_data):
        new_position = PositionModel(**position_data)
        self.db.add(new_position)
        self.db.commit()
        self.db.refresh(new_position)
        return new_position

    def update_position(self, position_id, position_data):
        position = self.get_position_by_id(position_id)
        if position:
            for key, value in position_data.items():
                setattr(position, key, value)
            self.db.commit()
            self.db.refresh(position)
            return position
        return None

    def delete_position(self, position_id):
        position = self.get_position_by_id(position_id)
        if position:
            self.db.delete(position)
            self.db.commit()
            return True
        return False