import React, { Component } from 'react'

class HookahDetail extends Component{
    render(){
        const obj = this.props.hookahDetail;
        return(
            // TODO move style to css
            <div style = {{ color: "yellow", border: "1px solid yellow"  }}>
                <h4>{obj.hookah_name}</h4>
                <h5>
                    Address: 
                        {obj.city}
                        {obj.street}
                        {obj.hookah_style}
                        {obj.hoojah_tobaco}
                        {/* {obj.hookah_images} */}
                    
                </h5>
            </div>
        )
    }
}

export default HookahDetail;