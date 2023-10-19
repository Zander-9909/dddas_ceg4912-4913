import React from "react";
import { StyleSheet, Text, View, SafeAreaView, Image } from "react-native";
import tw from 'tailwind-react-native-classnames';
import NavOptions from "../components/NavOptions";
import { GooglePlacesAutocomplete } from 'react-native-google-places-autocomplete';
import { GOOGLE_MAPS_APIKEY } from "@env";
import { useDispatch } from "react-redux";
import { setOrigin, setDestination } from "../slices/navSlice";

const HomeScreen = () => {
    const dispatch = useDispatch();

    return (
        <SafeAreaView style={tw`bg-white h-full`}>
            <View style = {tw`p-5`}>
                <Image
                    style = {{
                        width: 100, 
                        height:100, 
                        resizeMode: 'contain',
                    }}
                    source={{
                        uri:'https://www.coolgenerator.com/Data/Textdesign/202310/13e6e62ace6df3ab85e5a9b794a729e4.png',
                    }}
                />
                <GooglePlacesAutocomplete
                    placeholder="Where From?"
                    styles={{
                        container: {
                            flex: 0,
                        },
                        textInput: {
                            fontSize: 18,
                        },
                    }}
                    onPress={(data, details = null) => {
                        console.log(data);
                        console.log(details);
                        dispatch(
                            setOrigin({
                                location: details.geometry.location,
                                description: data.description,
                            })
                        );
                        dispatch(setDestination(null))
                    }}
                    fetchDetails = {true}
                    returnKeyType = {"search"}
                    //Get Rid of the google logo
                    enablePoweredByContainer={false}
                    //min length of place
                    minLength={2}
                    query = {{
                        key: {GOOGLE_MAPS_APIKEY},
                        language: 'en',
                    }} 
                    nearbyPlacesAPI="GooglePlacesSearch"
                    //wait 400 ms to search instead of searching immideiatly
                    debounce = {400}
                />
                <NavOptions/>
            </View>
        </SafeAreaView>
    );
};
export default HomeScreen;
const styles = StyleSheet.create({
    text:{
        color: 'blue'
    },
});