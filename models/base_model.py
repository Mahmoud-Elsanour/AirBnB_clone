#!/usr/bin/python3
"""
Defines the base model
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Difinition of all attributes and methods that are common with other
    classes and makes a link to File_Storage moduel
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel instance
        """
        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """
        Return the string representation
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save instance updates
        """
        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """
        Return the dictionary representation
        """
        self_dict = dict(self.__dict__)
        self_dict.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.created_at.isoformat()})
        return self_dict
