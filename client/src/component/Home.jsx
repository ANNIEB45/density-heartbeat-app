import React, { Component } from 'react'
import axios from 'axios'

export default class Home extends Component {
    state = {
        sensors: []
    }

    componentDidMount() {
        this.getSensorData()
    }

    getSensorData = async () => {
        try {
            const res = await axios.get('/api/v1/feed/')
            const newState = { ...this.state }
            newState.sensors = res.data
            // console.log(res.data)
            this.setState(newState)
            console.log('are we getting data')
        } catch (err) {
            console.log('Error getting all sensors')
            console.log(err)
        }
    }


// data not rendering on page??? 
    // getting status 404 error

    
    render() {
        return (
            // console.log(this.state.sensors)
            <div>
                <h1>Home Page</h1>
                { this.state.sensors.map((sensor) => {
                    return (
                        <div>
                            { sensor.name }
                            { sensor.location }
                            { sensor.heartbeat }
                        </div>
                    )
                }) }
            </div>
        )
    }
}
