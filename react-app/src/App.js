import React, { useEffect } from "react";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
// import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import { authenticate } from "./store/session";
import LandingPage from "./components/LandingPage/LandingPage";
import SignupPage from "./components/SignupPage/SignupPage";
import LoginPage from "./components/LoginPage/Login";
import Feed from "./components/Feed/Feed";
import NavigationBar from './components/NavigationBar/NavigationBar';
import './App.css';

function App() {
  // const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      // setLoaded(true);
    })();
  }, [dispatch]);

  if (!sessionUser) {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" exact={true}>
            <LandingPage />
          </Route>
          <Route path="/signup" exact={true}>
            <SignupPage />
          </Route>
          <Route path="/login" exact={true}>
            <LoginPage />
          </Route>
        </Switch>
      </BrowserRouter>
    );
  }

  return (
    <BrowserRouter>
      <div className="top-container">
        <Switch>
          <Route path="/login" exact={true}>
            <Redirect to="/" />
          </Route>
          <Route path="/signup" exact={true}>
            <Redirect to="/" />
          </Route>
          <ProtectedRoute path="/users" exact={true}>
            <UsersList />
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true}>
            <User />
          </ProtectedRoute>
          <ProtectedRoute path="/" exact={true}>
            <Feed />
          </ProtectedRoute>
        </Switch>
        <NavigationBar />
      </div>
    </BrowserRouter>
  );
}

export default App;
