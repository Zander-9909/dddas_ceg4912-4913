import { StyleSheet, Text, View} from 'react-native'
import React, { useEffect, useRef } from 'react'
import tw from 'tailwind-react-native-classnames';
import MapView, {Marker} from 'react-native-maps';
import { useSelector } from 'react-redux';
import { selectDestination, selectOrigin , selectWaypoint} from '../slices/navSlice';
import MapViewDirections from 'react-native-maps-directions';
import { GOOGLE_MAPS_APIKEY } from "@env";

const Map = () => {
    //pull information from the data layer
    const origin = useSelector(selectOrigin)
    const destination = useSelector(selectDestination)
    const waypoint = useSelector(selectWaypoint)
    const mapRef = useRef(null);

    /* Notes on waypoints
    it is impossible to have a placeholder then add a waypoint after routing
    the route MUST be drawn when all location are ready
    */

    //updates map based on changes in markers and added routes
    useEffect(() => {
        //checks origin and dest change
        if (!origin || !destination || !mapRef.current) {
            return;
        }
        const origin = {
            location: {
              lat: origin.location.lat,
              lng: origin.location.lng
            }
          };
        // This will zoom out the map to make sure all markers are visible
        mapRef.current.fitToCoordinates( [{ latitude: origin.location.lat, longitude: origin.location.lng }, 
            { latitude: destination.location.lat, longitude: destination.location.lng }] , { 
            edgePadding: { top: 50, right: 50, bottom: 50, left: 50 }, animated: true,
        });
    }, [origin, destination, waypoint]);

  return (
    <MapView
        ref={mapRef}
        style={tw`flex-1`}
        mapType="mutedStandard"
        initialRegion={{
            latitude: origin?.location.lat || 0,
            longitude: origin?.location.lng || 0,
            latitudeDelta: 0.05,
            longitudeDelta: 0.05,
        }}
    >
        {origin && destination && waypoint &&(
            <MapViewDirections
                origin={origin.description}
                destination={destination.description}
                waypoints={[waypoint.description]}
                apikey= {GOOGLE_MAPS_APIKEY}
                strokeWidth={3}
                strokeColor='black'
            />
        )}
        {origin?.location && (
            <Marker
                coordinate={{
                    latitude: origin.location.lat,
                    longitude: origin.location.lng,
                }}
                title ="Origin"
                description={origin.description}
                identifier='origin'
            />
        )}
        {destination?.location && (
            <Marker
                coordinate={{
                    latitude: destination.location.lat,
                    longitude: destination.location.lng,
                }}
                title ="destination"
                description={destination.description}
                identifier='destination'
            />
        )}
        {waypoint?.location && (
            <Marker
                coordinate={{
                    latitude: waypoint.location.lat,
                    longitude: waypoint.location.lng,
                }}
                title ="waypoint"
                description={waypoint.description}
                identifier='waypoint'
            />
        )}
    </MapView>
  );
};

export default Map

const styles = StyleSheet.create({})