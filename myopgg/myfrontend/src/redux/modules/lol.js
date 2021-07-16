
const SET_TIER = "SET_TIER";
const SET_RAGE = "SET_RAGE";
const SET_INGAME = "SET_INGAME";

function setTier(Tier) {
  return {
	type: SET_TIER,
	Tier
	};
}

function setRate(Rate) {
	return {
		type: SET_RATE,
		Rate
	};
}

function setIngame(Ingame) {
	return {
		type: SET_INGAME,
		Ingame
	}
}

function getTier(summoner_name) {
  return (dispatch, getState) => {
      fetch("/lol/tier/?summoner_name="+summoner_name, {
	      })
			.then(response => {
				return response.json();
			})
			.then(json => {
				dispatch(setTier(json));
			});
	};
}



function getRate(summoner_name) {
  return (dispatch, getState) => {
      fetch("/lol/rate/?summoner_name="+summoner_name, {
	      })
		        .then(response => {
				        return response.json();
						      })
							        .then(json => {
									        dispatch(setRate(json));
											      });
												    };
													}


function getIngame(summoner_name) {
													  return (dispatch, getState) => {
													      fetch("/lol/ingame/?summoner_name="+summoner_name, {
														      })
															        .then(response => {
																	        return response.json();
																			      })
																				        .then(json => {
																						        dispatch(setIngame(json));
																								      });
																									    };
																										}





const initialState = {};

function reducer(state = initialState, action) {
  switch (action.type) {
      case SET_TIER:
	        return applySetTier(state, action);
			    default:
				      return state;
	}
}



function applySetTier(state, action) {

const { Tier } = action;

	return {
		...state,
		Tier
	};
}



function applySetRate(state, action) {
  const { Rate } = action;
    return {
	    ...state,
		    Rate
			  };
			  }

function applySetIngame(state, action) {
			    const { Ingame } = action;
				  return {
				      ...state,
					      Ingame
						    };
							}



const actionCreators = {
	getTier,
};

export { actionCreators };

export default reducer;


