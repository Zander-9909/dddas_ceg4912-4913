import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons'

// screens
import NavigationScreen from './screens/NavigationScreen';
import AlertsScreen from './screens/AlertsScreen';
import StatsScreen from './screens/StatsScreen';
import SettingsScreen from './screens/SettingsScreen';

// screen names
const navigationName = 'Navigation';
const alertsName = 'Alerts';
const statsName = 'Stats';
const settingsName = 'Settings'

const Tab = createBottomTabNavigator();

function MainContainer() {
    return (
        <NavigationContainer>
            <Tab.Navigator
                initialRouteName={navigationName}
                screenOptions={({ route }) => ({
                    // tab bar styling
                    tabBarActiveTintColor: 'tomato',
                    tabBarInactiveTintColor: 'grey',
                    // tabBarLabelStyle: { paddingBottom: 10, fontSize: 10 },
                    // tabBarStyle: { padding: , height:  },
                    // tab bar icon select
                    tabBarIcon: ({ focused, color, size }) => {
                        let iconName;
                        let rn = route.name;
                        switch (rn) {
                            case navigationName:
                                iconName = focused ? 'home' : 'home-outline';
                                break;
                            case alertsName:
                                iconName = focused ? 'list' : 'list-outline';
                                break;
                            case statsName:
                                iconName = focused ? 'stats-chart' : 'stats-chart-outline';
                                break;
                            case settingsName:
                                iconName = focused ? 'settings' : 'settings-outline';
                                break;
                        }
                        return <Ionicons name={iconName} size={size} color={color} />

                    },
                })}>
                
                <Tab.Screen name={navigationName} component={NavigationScreen} />
                <Tab.Screen name={alertsName} component={AlertsScreen} />
                <Tab.Screen name={statsName} component={StatsScreen} />
                <Tab.Screen name={settingsName} component={SettingsScreen} />

            </Tab.Navigator>
        </NavigationContainer>
    );
}

export default MainContainer;
// might need to clear cache react-native start --reset-cache