import os
import streamlit.components.v1 as components

_component_func = components.declare_component(
    # We give the component a simple, descriptive name ("my_component"
    # does not fit this bill, so please choose something better for your
    # own component :)
    "nevermined",
    # Pass `url` here to tell Streamlit that the component will be served
    # by the local dev server that you run via `npm run start`.
    # (This is useful while your component is in development.)
    url="http://localhost:3000/streamlit"
)

def nevermined(did=None):
    """Creates a new instance of "nevermined" component.

    Parameters
    ----------
    did: str
        The did of the subscription.

    Returns
    -------
    str
        An auth token or 0 (zero) if user is not authenticated
    """
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(did=did, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
