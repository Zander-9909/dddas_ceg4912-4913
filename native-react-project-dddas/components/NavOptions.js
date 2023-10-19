import { useNavigation } from '@react-navigation/native';
import React from 'react'
import { Text, View, Image, FlatList, TouchableOpacity } from 'react-native'
import { Icon } from 'react-native-elements';
import { useSelector } from 'react-redux';
import tw from "tailwind-react-native-classnames";
import { selectDestination, selectOrigin } from '../slices/navSlice';

const data = [
    {
        id: "123",
        title: "Start Trip",
        image: "https://www.pngall.com/wp-content/uploads/5/Delivery-Truck-PNG-Clipart.png",
        screen: "MapScreen"
    },
    {
        id: "456",
        title: "Analytics",
        image: "https://www.aihr.com/wp-content/uploads/People-Analytics-Main-Cover.png",
        screen: "AnalyticsScreen"
    },
];
const NavOptions = () => {
    const navigation = useNavigation();
    //pull info from datalayer for select origin
    const origin = useSelector(selectOrigin);
    return (
        <FlatList
            data={data}
            horizontal
            keyExtractor={(item) => item.id}
            renderItem={({ item, index }) => (
                <TouchableOpacity
                    onPress={() => navigation.navigate(item.screen)}
                    style={tw`p-2 pl-6 pb-8 pt-4 bg-gray-200 m-2 w-40`}
                    //Disable if orgin is not entered
                    disabled = {!origin && index === 0}
                    // Only display buttons if origin is selected
                    >
                    <View style={tw`${!origin && index === 0 ? "opacity-20" : ""}`}>
                        <Image
                            style={{ width: 120, height: 120, resizeMode: "contain" }}
                            source={{ uri: item.image }}
                        />
                        <Text style={tw`mt-2 text-lg font-semibold`}>{item.title}</Text>
                        <Icon
                            style={tw`p-2 bg-black rounded-full w-10 mt-4`}
                            name="arrowright"
                            color="white"
                            type="antdesign"
                        />
                    </View>
                </TouchableOpacity>
            )}
        />
    );
};

export default NavOptions
