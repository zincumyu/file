using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour{
    public Transform player
    private float MOUSEX,MOUSEY;
    public float MOUSEspeed; //灵敏度
    public float XR;

    private void Update ()  {
        MOUSEX =Input.GetAxis ("Mouse X") * MOUSEspeed * Time.deltaTime;
        MOUSEY =Input.GetAxis ("Mouse Y") * MOUSEspeed * Time.deltaTime;
        XR -=MOUSEY;
        XR =Mathf.Clamp(XR,-70f,70f);
        player.Rotate  (Vector3.up * MOUSEX);
        transform.localRotation =Quaternion.Euler( XR,0,0);
    }
}

