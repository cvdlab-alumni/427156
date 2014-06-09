        function createText(){
          var P2 = new THREE.MeshPhongMaterial({color: 0xff5555});
          var textGeom = new THREE.TextGeometry( 'Penne', {font:'helvetiker', size:12,height:1, weight:'bold'});
          var textMesh = new THREE.Mesh( textGeom, P2 );
          textMesh.rotation.order = "ZXY"
          textMesh.rotation.z = Math.PI;
          textMesh.rotation.x = Math.PI/2;

          textMesh.castShadow = true;
          return textMesh;

        }

        function createTable(x,y,z){

          var pianoGeometry = new THREE.BoxGeometry(x,y,2,20,20,20);
          var pianoMaterial = new THREE.MeshPhongMaterial({color: 0x7777ff,shininess: 0, wireframe:false,receiveShadow:true});
          var piano = new THREE.Mesh(pianoGeometry,pianoMaterial);
          var zampaGeometry = new THREE.BoxGeometry(x/10,y/10,z,5,5,10);
          var zampaMaterial = new THREE.MeshLambertMaterial({color: 0x7777ff, wireframe:false});
          var zampa1 = new THREE.Mesh(zampaGeometry,zampaMaterial);
          var zampa2 = new THREE.Mesh(zampaGeometry,zampaMaterial);
          var zampa3 = new THREE.Mesh(zampaGeometry,zampaMaterial);
          var zampa4 = new THREE.Mesh(zampaGeometry,zampaMaterial);
          zampa1.position.set((-x/2 + x/20),(-y/2 + y/20),(-z / 2 -2));
          zampa2.position.set((-x/2 + x/20),(y/2 - y/20),(-z / 2 -2));
          zampa3.position.set((x/2 - x/20),(y/2 - y/20),(-z / 2 -2));
          zampa4.position.set((x/2 - x/20),(-y/2 + y/20),(-z / 2 -2));
          
          piano.receiveShadow = true;
          piano.castShadow = true;
          piano.position.set(0,0,-1)
          var tavolo = new THREE.Object3D();
          tavolo.add(zampa1);
          tavolo.add(zampa2);
          tavolo.add(zampa3);
          tavolo.add(zampa4);
          tavolo.add(piano); 

          tavolo.xMax = x/2 - 9;
          tavolo.yMax = y/2 - 9;
          
          return tavolo; 
        }

                function createLamp(){

          var baseLampGeometry = new THREE.CylinderGeometry( 9, 7, 2, 32 ); 
          var baseLampMaterial = new THREE.MeshPhongMaterial({color: 0xc6c6c6, shininess: 80, specular: 0xc6c6c6, wireframe: false, metal:true});
          var baseLamp = new THREE.Mesh(baseLampGeometry,baseLampMaterial);
          baseLamp.rotation.x=-0.5*Math.PI;
          var lamp = new THREE.Object3D();
          baseLamp.castShadow = true;
          baseLamp.receiveShadow = true;
          lamp.add(baseLamp);

          var nodoBaseGeometry = new THREE.SphereGeometry(2,32,32,0,2*Math.PI);
          var pivot1 = new THREE.Mesh(nodoBaseGeometry,new THREE.MeshPhongMaterial({
            color: 0x262626,
            shininess: 50,
            specular: 0xbfa53f,
            wireframe: false, metal:true}));
          pivot1.castShadow = true;
          pivot1.receiveShadow = true;
          pivot1.position.set(0,0,1);

          var arm1Geometry = new THREE.CylinderGeometry(0.75,0.75,15,32);
          var arm1 = new THREE.Mesh(arm1Geometry,baseLampMaterial);
          arm1.rotation.x=-0.5*Math.PI;
          arm1.position.set(0,0,9.2);
          arm1.castShadow = true;
          arm1.receiveShadow = true;
          pivot1.add(arm1);

          var pivot2 = new THREE.Mesh(new THREE.SphereGeometry(1.2,32,32,0,2*Math.PI),new THREE.MeshPhongMaterial({
            color: 0x262626,
            shininess: 50,
            specular: 0xbfa53f,
            wireframe: false, metal:true}));
          pivot2.castShadow = true;
          pivot2.receiveShadow = true;

          var arm2 = new THREE.Mesh(new THREE.CylinderGeometry(0.75,0.75,15,32), baseLampMaterial);
          arm2.rotation.x=-0.5*Math.PI;
          arm2.position.set(0,0,8);
          arm2.castShadow = true;
          arm2.receiveShadow = true;
          pivot2.add(arm2);
          pivot2.position.set(0,0,16.75);
          pivot1.add(pivot2);
          
          var pivot3 = new THREE.Mesh(new THREE.SphereGeometry(1.2,32,32,0,2*Math.PI),new THREE.MeshPhongMaterial({
            color: 0x262626,
            shininess: 50,
            specular: 0xbfa53f,
            wireframe: false, metal:true}));
          pivot3.position.set(0,0,16);
          pivot3.castShadow = true;
          pivot3.receiveShadow = true;

          var plafonieraGeometry = new THREE.SphereGeometry(5,32,32,0,Math.PI);
          var plafonieraMaterial = new THREE.MeshPhongMaterial({color: 0xc6c6c6,blending:THREE.AdditiveBlending, shininess: 80, specular: 0xc6c6c6, wireframe: false, side: THREE.DoubleSide, metal:true});

          var plafoniera = new THREE.Mesh(plafonieraGeometry,plafonieraMaterial);
          plafoniera.rotation.x=Math.PI;
          plafoniera.position.set(0,0,6);
          plafoniera.castShadow = true;
          plafoniera.receiveShadow = true;

          var bulbGeometry = new THREE.SphereGeometry(2,32,32);
          var bulbMaterial = new THREE.MeshPhongMaterial({color: 0xffef47, transparent:true, opacity:0.5,  wireframe: false});
          var bulb = new THREE.Mesh(bulbGeometry,bulbMaterial);
          bulb.castShadow = true;
          var cilindroGeometry = new THREE.CylinderGeometry(0.8,0.6,1,16);
          var cilindroMaterial = new THREE.MeshPhongMaterial({color:0x7a7a7a});
          var cilindro = new THREE.Mesh(cilindroGeometry,cilindroMaterial);

          bulb.position.set(0,0,4);
          cilindro.rotation.x=-0.5*Math.PI;
          cilindro.position.set(0,0,4.5);
          cilindro.castShadow = true;
          plafoniera.add(cilindro);

          pivot3.add(plafoniera);

          var spotlight = new THREE.SpotLight(0xfffa72, 2);
          spotlight.castShadow = true;
          spotlight.position.set(0,0,2);
          //spotlight.shadowCameraVisible = true;
          var lightTarget = new THREE.Object3D();
          lightTarget.position.set(0,0,6);
          bulb.add(lightTarget);
          spotlight.target = lightTarget;
          spotlight.shadowDarkness = .8;
          spotlight.shadowCameraNear = 1;
          spotlight.shadoCameraFar = 5000;
          spotlight.shadowCameraFov = 170;
          spotlight.shadowMapWidth = 2048;
          spotlight.shadowMapHeight = 2048;
         

          spotlight.angle = Math.PI*1.5;
          spotlight.exponent = 1;
          

          var pointLight = new THREE.PointLight(0xfffa72, 2, 5);
          bulb.add(pointLight);
          bulb.add(spotlight);


          pivot3.add(bulb);

          pivot2.add(pivot3);

          lamp.add(pivot1);
          pivot1.rotation.order = "ZXY"
         /* pivot1.rotation.x=-.2*Math.PI;
          pivot1.rotation.z=.5*Math.PI;
          pivot2.rotation.x= Math.PI*.5;
          pivot3.rotation.x=Math.PI*.5; */
          
          lamp.pivot3 = pivot3;
          lamp.pivot2 = pivot2;
          lamp.pivot1 = pivot1;
          lamp.light1 = spotlight;
          lamp.light2 = pointLight;

          var SLHelper = new THREE.SpotLightHelper(spotlight,20);
          //scene.add(SLHelper);
          return lamp;

        }