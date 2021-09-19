import React from 'react';
import styles from './BotAvatar.css'
import bot_avatar from '../../../assets/bot_avatar.png';
const BotAvatar = () =>{
    return(
        <div className="avatar">
            <img className="avatar_img"  src={bot_avatar} style={styles.avatar_img} alt="" />
        </div>
    )
}

export default BotAvatar;