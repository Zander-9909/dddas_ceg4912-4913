import { StyleSheet, Text, View } from 'react-native'
import React, { useEffect, useRef } from 'react'
import tw from 'tailwind-react-native-classnames';
import MapView, {Marker} from 'react-native-maps';
import { useSelector } from 'react-redux';
import { selectDestination, selectOrigin } from '../slices/navSlice';
import MapViewDirections from 'react-native-maps-directions';
import { GOOGLE_MAPS_APIKEY } from "@env";

const fetchRestStopsAlongRoute = async (origin, destination) => {
    try {
      const directionResponse = await fetch(
        `https://maps.googleapis.com/maps/api/directions/json?origin=${origin}&destination=${destination}&key=${GOOGLE_MAPS_API_KEY}`
      );
      const directionData = await directionResponse.json();
  
      if (directionData.routes.length > 0) {
        const route = directionData.routes[0];
        const waypoints = route.legs[0].steps
          .filter(step => step.travel_mode === 'DRIVING')
          .map(step => ({
            latitude: step.end_location.lat,
            longitude: step.end_location.lng,
          }));
  
        const restStops = await Promise.all(
          waypoints.map(async waypoint => {
            try {
              const placesResponse = await fetch(
                `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${waypoint.latitude},${waypoint.longitude}&radius=10000&type=rest_stop&key=${GOOGLE_MAPS_API_KEY}`
              );
              const placesData = await placesResponse.json();
              return placesData.results.map(place => ({
                name: place.name,
                location: place.geometry.location,
              }));
            } catch (error) {
              console.error('Error fetching places:', error);
              return [];
            }
          })
        );
  
        return restStops.flat();
      }
    } catch (error) {
      console.error('Error fetching directions:', error);
      return [];
    }
  };
const Map = () => {
    //pull information from the data layer
    const origin = useSelector(selectOrigin)
    const destination = useSelector(selectDestination)
    const mapRef = useRef(null);
    //updates when orgin or destination is changed
    useEffect(() => {
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
    }, [origin, destination]);

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
        {origin && destination &&(
            <MapViewDirections
                origin={origin.description}
                destination={destination.description}
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
    </MapView>
  );
};

export default Map

const styles = StyleSheet.create({})