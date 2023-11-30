import React, { useEffect, useRef } from 'react'
import { SafeAreaView, StyleSheet, Text, View, KeyboardAvoidingView, Platform, Button} from 'react-native';
import tw from 'tailwind-react-native-classnames';
import { GooglePlacesAutocomplete } from 'react-native-google-places-autocomplete';
import { GOOGLE_MAPS_APIKEY } from "@env";
import { useDispatch, useSelector } from 'react-redux';
import { useNavigation } from '@react-navigation/native';
import { setWaypoint } from '../slices/navSlice';
import { selectDestination, selectOrigin , selectWaypoint} from '../slices/navSlice';

const RideOptionsCard = () => {
  const dispatch = useDispatch();
  const navigation = useNavigation();
  const origin = useSelector(selectOrigin)
  const destination = useSelector(selectDestination)
  const waypoint = useSelector(selectWaypoint)
  const mapRef = useRef(null);
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
    /* Pick the alternate onroute location to stop at
    -recalc the route needs impl
    */
    <SafeAreaView style={tw`bg-white flex-1`}>
      <Text style={tw`text-center py-5 text-xl`}>Pick truck stops</Text>
      <KeyboardAvoidingView
                behavior={Platform.OS === "ios" ? "padding" : "height"}
                style={{ flex: 1 }}
                keyboardVerticalOffset={Platform.OS === "ios" ? 0 : 20}
            >
                <View style={tw`border-t border-gray-200 flex-shrink`}>
                    <GooglePlacesAutocomplete
                        placeholder="Select truck stop"
                        styles={styles}
                        fetchDetails={true}
                        returnKeyType={"search"}
                        minLength={2}
                        onPress={(data, details = null) => {
                            dispatch(
                                setWaypoint({
                                    location: details.geometry.location,
                                    description: data.description,
                                })
                            );
                            navigation.navigate("RideOptionsCard");
                        }}
                        enablePoweredByContainer={false}
                        query={{
                            key: GOOGLE_MAPS_APIKEY,
                            language: "en",
                        }}
                        nearbyPlacesAPI='GooglePlacesSearch'
                        debounce={400}
                    />
                </View>
            </KeyboardAvoidingView>
    </SafeAreaView>
  )
}

export default RideOptionsCard

const styles = StyleSheet.create({
    container: {
      backgroundColor: "white",
      paddingTop: 20,
      flex: 0,
  },
  textInput: {
      backgroundColor: "#DDDDDF",
      borderRadius: 0,
      fontSize: 18,
  },
  textInputContainer: {
      paddingHorizontal: 20,
      paddingBottom: 0,
  },
});