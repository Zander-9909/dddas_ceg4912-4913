import React from 'react';
import { Provider } from "react-redux";
import { store } from './store';
import { SafeAreaProvider } from "react-native-safe-area-context";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from '@react-navigation/stack';

// Import screens from both snippets
import ForgotPasswordScreen from './screens/ForgotPasswordScreen';
import SigninScreen from './screens/SigninScreen';
import RegisterScreen from './screens/RegisterScreen';
import HomeScreen from "./screens/HomeScreen";
import MapScreen from "./screens/MapScreen";
import AnalyticsScreen from "./screens/AnalyticsScreen";

// Define Stack Navigator
const Stack = createStackNavigator();

function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <SafeAreaProvider>
          <Stack.Navigator>

            {/* Screens from the first snippet */}
            <Stack.Screen name='Signin' component={SigninScreen} options={{ headerShown: false }} />
            <Stack.Screen name='Register' component={RegisterScreen} />
            <Stack.Screen name='ForgotPassword' component={ForgotPasswordScreen} />

            {/* Screens from the second snippet */}
            <Stack.Screen name='HomeScreen' component={HomeScreen} options={{ headerShown: false }} />
            <Stack.Screen name='MapScreen' component={MapScreen} options={{ headerShown: false }} />
            <Stack.Screen name='AnalyticsScreen' component={AnalyticsScreen} options={{ headerShown: false }} />

          </Stack.Navigator>
        </SafeAreaProvider>
      </NavigationContainer>
    </Provider>
  );
}

export default App;
