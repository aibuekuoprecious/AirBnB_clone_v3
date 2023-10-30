#!/usr/bin/python3
"""places_amenities"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from datetime import datetime
import uuid
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    @app_views.route('/places/<place_id>/amenities', methods=['GET'])
    @app_views.route('/places/<place_id>/amenities/', methods=['GET'])
    def list_amenities_of_place(place_id):
        ''' Retrieves a list of all Amenity objects of a Place '''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)
        amenity_list = []
        for obj in all_places:
            if obj.id == place_id:
                for amenity in obj.amenities:
                    amenity_list.append(amenity.to_dict())
        return jsonify(amenity_list)

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['POST'])
    def create_place_amenity(place_id, amenity_id):
        '''Creates a Amenity'''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)

        all_amenities = storage.all("Amenity").values()
        amenity_data = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        if amenity_data == []:
            abort(404)

        amenities = []
        for place in all_places:
            if place.id == place_id:
                for amenity in all_amenities:
                    if amenity.id == amenity_id:
                        place.amenities.append(amenity)
                        storage.save()
                        amenities.append(amenity.to_dict())
                        return jsonify(amenities[0]), 200
        return jsonify(amenities[0]), 201

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['DELETE'])
    def delete_place_amenity(place_id, amenity_id):
        '''Deletes a Amenity object'''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)

        all_amenities = storage.all("Amenity").values()
        amenity_data = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        if amenity_data == []:
            abort(404)
        amenity_data.remove(amenity_data[0])

        for obj in all_places:
            if obj.id == place_id:
                if obj.amenities == []:
                    abort(404)
                for amenity in obj.amenities:
                    if amenity.id == amenity_id:
                        storage.delete(amenity)
                        storage.save()
        return jsonify({}), 200
"""
else:
    @app_views.route('/places/<place_id>/amenities', methods=['GET'])
    @app_views.route('/places/<place_id>/amenities/', methods=['GET'])
    def list_amenities_of_place(place_id):
        ''' Retrieves a list of all Amenity objects of a Place '''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)
        amenity_list = []
        for obj in all_places:
            if obj.id == place_id:
                for amenity in obj.amenities:
                    amenity_list.append(amenity.to_dict())
        return jsonify(amenity_list)

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['POST'])
    def create_place_amenity(place_id, amenity_id):
        '''Creates a Amenity'''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)

        all_amenities = storage.all("Amenity").values()
        amenity_data = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        if amenity_data == []:
            abort(404)

        amenities = []
        for place in all_places:
            if place.id == place_id:
                for amenity in all_amenities:
                    if amenity.id == amenity_id:
                        place.amenities.append(amenity)
                        storage.save()
                        amenities.append(amenity.to_dict())
                        return jsonify(amenities[0]), 200
        return jsonify(amenities[0]), 201

    @app_views.route('/places/<place_id>/amenities/<amenity_id>',
                     methods=['DELETE'])
    def delete_place_amenity(place_id, amenity_id):
        '''Deletes a Amenity object'''
        all_places = storage.all("Place").values()
        place_data = [obj.to_dict() for obj in all_places if obj.id == place_id]
        if place_data == []:
            abort(404)

        all_amenities = storage.all("Amenity").values()
        amenity_data = [obj.to_dict() for obj in all_amenities
                       if obj.id == amenity_id]
        if amenity_data == []:
            abort(404)
        amenity_data.remove(amenity_data[0])

        for obj in all_places:
            if obj.id == place_id:
                if obj.amenities == []:
                    abort(404)
                for amenity in obj.amenities:
                    if amenity.id == amenity_id:
                        storage.delete(amenity)
                        storage.save()
        return jsonify({}), 200
"""


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_place_amenity(amenity_id):
    '''Retrieves a Amenity object '''
    all_amenities = storage.all("Amenity").values()
    amenity_data = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_data == []:
        abort(404)
    return jsonify(amenity_data[0])
