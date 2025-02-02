import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import session from "./session";
import postsReducer from "./posts";
// import likesReducer from "./likes";
import commentsReducer from "./comments";
import followersReducer from "./followers";
import followingReducer from "./following";
import followsReducer from "./follows";

const rootReducer = combineReducers({
  session,
  posts: postsReducer,
  // likes: likesReducer,
  comments: commentsReducer,
  followers: followersReducer,
  following: followingReducer,
  follows: followsReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require("redux-logger").default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
