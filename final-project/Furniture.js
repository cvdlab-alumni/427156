 function insertFurniture(scene){
  var loaderOBJ = new THREE.OBJLoader();
  //loaderOBJMTL = new THREE.OBJMTLLoader();
  loaderOBJ.load('assets/models/soderhamn1.obj', function(obj){


    var material = [new THREE.MeshLambertMaterial({color: 0xFFF7C2, side: THREE.DoubleSide, shading: THREE.FlatShading, castShadow:true,receiveShadow:true})];
    var material1 = [new THREE.MeshLambertMaterial({color: 0x030769, side: THREE.DoubleSide, shading: THREE.FlatShading, castShadow:true,receiveShadow:true})]

    var sofa = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, material);
    for(var i = 0; i < obj.children.length; i++){
      if(i<=3){
        sofa.add(THREE.SceneUtils.createMultiMaterialObject(obj.children[i].geometry,material1));
      }else{
        sofa.add(THREE.SceneUtils.createMultiMaterialObject(obj.children[i].geometry,material));
      }
    }
    sofa.rotation.x = Math.PI*0.5;
    sofa.scale.set(10,10,10);
    sofa.position.set( 24,34,2);

    scene.add(sofa);
  });

  //var loaderOBJ = new THREE.OBJLoader();
  loaderOBJ.load('assets/models/diningTable.obj', function(obj){
    //global_o = obj;

    var material = [new THREE.MeshPhongMaterial({color: 0x592A0B , side: THREE.DoubleSide, shading: THREE.FlatShading, castShadow:true,receiveShadow:true})];
    material[0].map = THREE.ImageUtils.loadTexture("assets/textures/wood-texture.jpg");
    var tavolo = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, material);
    tavolo.rotation.x = Math.PI*0.5;
    tavolo.scale.set(0.09,0.09,0.11);
    tavolo.position.set(78,40,1);
    scene.add(tavolo);
  });


  addOBJMTL(scene,'cucina',[11,63,1],[0.1, 0.1, 0.1],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'lavello',[11,49,1],[0.1, 0.1, 0.1],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'doppio',[2,49,1],[0.1, 0.1, 0.1],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'doppio',[-10.3,49,1],[0.22, 0.1, 0.1],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'fridge',[9,41,5],[12, 12, 12],[-Math.PI*0.5,0,Math.PI]);
  addOBJMTL(scene,'cappa',[7,66,18],[2, 2, 2],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'water',[78,99,1],[0.1,0.1,0.1],[-Math.PI*0.5,Math.PI,Math.PI,'XZY']);
  addOBJMTL(scene,'bathroomFurniture',[94,99,1],[0.1,0.1,0.1],[-Math.PI*0.5,-Math.PI/2,Math.PI,'XZY']);
  addOBJMTL(scene,'lit',[122,22,4],[0.08, 0.08, 0.08],[Math.PI*0.5,0,0]);
  addOBJMTL(scene,'armoireLotus',[115,8,9.8],[0.08, 0.08, 0.08],[Math.PI*0.5,Math.PI,0]);
  
  var painting = createPainting('x',8,6,'vangogh');
  painting.position.set(73,69,10);
  scene.add(painting);

  var portaGeom = new THREE.BoxGeometry(2.5,0.8,16);
  var mesh = createBumpMesh(portaGeom,"door.jpg","door-bump.jpg");
  mesh.position.set(66.25,104.5,9);
  scene.add(mesh);


  return;
}

function addOBJMTL(scene,nomeMod,pos,scale,rotation){

  var loaderOBJMTL = new THREE.OBJMTLLoader();
  loaderOBJMTL.addEventListener('load',function(event){
    var obj = event.content;
    obj.rotation.set(rotation[0],rotation[1],rotation[2]);
    obj.scale.set(scale[0],scale[1],scale[2]);
    obj.position.set(pos[0],pos[1],pos[2]);
    mesh = obj;
    scene.add(mesh);
  });

  loaderOBJMTL.load('assets/models/'+nomeMod+'.obj','assets/models/'+nomeMod+'.mtl', {
        side: THREE.DoubleSide, castShadow:true, receiveShadow:true });


}

function mkTV(){
  //TV
  video = document.createElement( 'video' );
  video.id = 'video';
  video.type = ' video/ogg; codecs="theora, vorbis" ';
  video.src = "videos/sintel.ogv";
  video.load(); // must call after setting/changing source
  //video.play();
  video.volume = 0.2;
  videoImage = document.createElement( 'canvas' );
  videoImage.width = 480;
  videoImage.height = 204;
  videoImageContext = videoImage.getContext( '2d' );
  // background color if no video present
  videoImageContext.fillStyle = '#000000';
  videoImageContext.fillRect( 0, 0, videoImage.width, videoImage.height );
  videoTexture = new THREE.Texture( videoImage );
  videoTexture.minFilter = THREE.LinearFilter;
  videoTexture.magFilter = THREE.LinearFilter;
  videoTexture.format = THREE.RGBFormat;


  var tvGeom = new THREE.BoxGeometry(10,0.5,5.625);
  var tvMat = new THREE.MeshPhongMaterial({color:0x000000, shininess: 50,  metal:true});
  var tvMesh = new THREE.Mesh(tvGeom,tvMat);
  tvMesh.isPlaying = false;
  tvMesh.interact = function(){
    if(!tvMesh.isPlaying){
      video.play();
      tvMesh.isPlaying = true;
    }else{
      video.pause();
      video.currentTime = 0;
      tvMesh.isPlaying= false;
    }
  }
  tvMesh.position.set(30,3.25,12);
  var schermoGeom = new THREE.PlaneGeometry(9.8,5.425,4,4);
  var schermoMat = new THREE.MeshBasicMaterial( { map: videoTexture, overdraw: true, side:THREE.DoubleSide } );
  var schermo = new THREE.Mesh(schermoGeom,schermoMat);
  schermo.rotation.x = Math.PI/2;
  schermo.rotation.y = Math.PI;
  schermo.position.set(0.05,0.26,0.05);
  tvMesh.add(schermo);
  return tvMesh;
}


function createPainting(asse,dimX,dimY,picture){
  var texture = THREE.ImageUtils.loadTexture("assets/textures/"+picture+".jpg");
  var geomTela = new THREE.PlaneGeometry(dimX,dimY,10,10);
  var matTela = new THREE.MeshPhongMaterial({map: texture, side: THREE.DoubleSide});

  var shape = new THREE.Shape();
  shape.moveTo(0,0);
  shape.lineTo(dimX,0);
  shape.lineTo(dimX,dimY);
  shape.lineTo(0,dimY);
  shape.lineTo(0,0);
  var pts = [];
  
  pts.push(new THREE.Vector2(0.5,0.5));
  pts.push(new THREE.Vector2(dimX-0.5,0.5));
  pts.push(new THREE.Vector2(dimX-0.5,dimY-0.5));
  pts.push(new THREE.Vector2(0.5,dimY-0.5));
  pts.push(new THREE.Vector2(0.5,0.5));

  var hole = new THREE.Path(pts);

  Tela = new THREE.Mesh(geomTela, matTela);

  shape.holes.push(hole);

  var corniceGeom = new THREE.ExtrudeGeometry(shape,{amount: 0.3, bevelEnabled: false});
  var cornice = new THREE.Mesh(corniceGeom,new THREE.MeshPhongMaterial({color: 0xFFDD00}));


  Tela.position.set(dimX/2,dimY/2,0.25);
  cornice.add(Tela);
  cornice.rotation.order = "ZXY";
  cornice.rotation.x = Math.PI*0.5;
  if(asse=="y"){
    cornice.rotation.z = Math.PI*0.5;
  }

return cornice;
}

/*function makeLampada(scene,pos){
  var lampGeom = new THREE.SphereGeometry(2,32,32,0,Math.PI);
  var lampMat = new THREE.MeshPhongMaterial({color: 0xc6c6c6,blending:THREE.AdditiveBlending, shininess: 80, specular: 0xc6c6c6, wireframe: false, side: THREE.DoubleSide, metal:true}); 
  var meshLampada = new THREE.Mesh(lampGeom,lampMat);

  var lampLight = new THREE.SpotLight();
  lampLight.castShadow = true;
  lampLight.position.set(0,0,0);
  var lightTarget = new THREE.Object3D();
  lightTarget.position.set(0,0,-1);
  lampLight.target = lightTarget;
  lampLight.add(lightTarget);
  meshLampada.add(lampLight);

  meshLampada.position.set(pos[0],pos[1],20);

  meshLampada.interact = function(){
    meshLampada.lampLigth.intensity = 0;
  }
  scene.add(meshLampada);

  return;
}*/