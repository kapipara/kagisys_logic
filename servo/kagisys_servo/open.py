# -*- coding: utf-8 -*-

"""This open the door lock."""


from model import servo_model
from model import storage_model


def main():
    """Open door lock."""
    servo = servo_model.Servo()
    servo.open()

    # update file
    storage = storage_model.StorageModel()
    storage.update_file("open")


if __name__ == '__main__':
    main()
