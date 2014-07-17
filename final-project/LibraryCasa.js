function texturePavimento(nomeTexture,dimX,dimY,posX,posY,repeatX,repeatY){
 var floor = createMesh(new THREE.BoxGeometry(dimX,dimY,0.1), nomeTexture);
 floor.material.map.repeat.set(repeatX,repeatY);
 floor.position.set(posX+(dimX/2),posY+(dimY/2),1.05);
 floor.receiveShadow = true;
 return floor;
}

function texturePavimentoBump(nomeTexture,nomeBump,dimX,dimY,posX,posY,repeatX,repeatY){
 var floor = createBumpMesh(new THREE.BoxGeometry(dimX,dimY,0.1), nomeTexture,nomeBump);
 //floor.material.map.repeat.set(repeatX,repeatY);
 //floor.material.bumpMap.repeat.set(repeatX,repeatY);
 floor.position.set(posX+(dimX/2),posY+(dimY/2),1.05);
 floor.receiveShadow = true;
 return floor;
}


function textureShape(shape,nomeTexture,repeatX,repeatY){
 var geomForma = new THREE.ExtrudeGeometry(shape,{amount:0.1,bevelEnabled: false});
 var floor = createMesh(geomForma, nomeTexture);
 floor.material.map.repeat.set(repeatX,repeatY);
 floor.position.set(0,0,1.05);
 floor.receiveShadow = true;
 return floor;
}

function textureShapeWall(shape,nomeTexture,repeatX,repeatY){
 var geomForma = new THREE.ExtrudeGeometry(shape,{amount:0.5,bevelEnabled: false});
 var floor = createMesh(geomForma, nomeTexture);
 floor.material.map.repeat.set(repeatX,repeatY);
 floor.rotation.x = Math.PI/2;

 floor.position.set(0,3,1.05);
 floor.receiveShadow = true;
 return floor;
}


function createMesh(geom, texture) {
var texture = THREE.ImageUtils.loadTexture("assets/textures/" + texture);
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;

geom.computeVertexNormals();
var mat = new THREE.MeshPhongMaterial();
mat.map = texture;

var mesh = new THREE.Mesh(geom, mat);

return mesh;
}

function createFinestra(asse,dimX,dimY){
  var geomVetro = new THREE.PlaneGeometry(dimX,dimY,10,10);
  var matVetro = new THREE.MeshPhongMaterial({color: 0xD9F4FA, transparent: true, opacity: 0.2, shininess: 80, side: THREE.DoubleSide});
  //var vetro = new THREE.Mesh(geomVetro,matVetro);
  //vetro.doubleSided = true;

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
  
  refractSphereCamera = new THREE.CubeCamera( 0.1, 5000, 512 );
  scene.add( refractSphereCamera );
    
  refractSphereCamera.renderTarget.mapping = new THREE.CubeRefractionMapping();
    
 

  vetro = new THREE.Mesh(geomVetro, matVetro);




  shape.holes.push(hole);

  var corniceGeom = new THREE.ExtrudeGeometry(shape,{amount: 0.5, bevelEnabled: false});
  var cornice = new THREE.Mesh(corniceGeom,new THREE.MeshPhongMaterial({color: 0x33160E}));


  vetro.position.set(dimX/2,dimY/2,0.25);
  cornice.add(vetro);
  cornice.rotation.order = "ZXY";
  cornice.rotation.x = Math.PI*0.5;
  if(asse=="y"){
    cornice.rotation.z = Math.PI*0.5;
  }

return cornice;
}

function createPorta(asse,openAngle,closeAngle){

  var cilGeom = new THREE.CylinderGeometry( 0.15, 0.15, 2, 16 );
  var cilMat = new THREE.MeshPhongMaterial({
            color: 0x262626,
            shininess: 50,
            specular: 0x262626,
            metal:true});
  var cilindro = new THREE.Mesh(cilGeom,cilMat);
  

  var manigliaGeom = new THREE.CylinderGeometry(0.15,0.15,1.5,16);
  var maniglia = new THREE.Mesh(manigliaGeom,cilMat);
  maniglia.rotation.z = Math.PI*0.5;
  maniglia.position.set(-0.5,1,0);
  cilindro.add(maniglia);
  var maniglia1 = maniglia.clone();
  maniglia1.position.y = -1;
  cilindro.add(maniglia1);

    var geom = new THREE.BoxGeometry(8,0.8,16);
    var mesh = createBumpMesh(geom,"door.jpg","door-bump.jpg");
    mesh.position.set(4,0.4,8);
    cilindro.position.set(3,0,-1);
    mesh.add(cilindro);

  mesh.isOpen = false;
  var cardine = new THREE.Object3D();
  cardine.position.y = 0.8;
  mesh.isPorta = true;
  cardine.add(mesh);
  if(asse == "y"){
    cardine.position.x = 1;
    cardine.rotation.z = Math.PI*0.5;
  }
  mesh.interact = function(){
    if(!mesh.isOpen){
      mesh.isOpen = true;
      var tween1 = new TWEEN.Tween(cardine.rotation).to({z: openAngle}, 1500).easing(TWEEN.Easing.Quadratic.InOut).delay(100).start();
      var tween2 = new TWEEN.Tween(cilindro.rotation).to({y: -Math.PI*0.3}, 1000).easing(TWEEN.Easing.Elastic.Out).start();
    }
    else{
      mesh.isOpen = false;
      var tween1 = new TWEEN.Tween(cardine.rotation).to({z: closeAngle}, 1500).easing(TWEEN.Easing.Quadratic.InOut).start();

      var tween2 = new TWEEN.Tween(cilindro.rotation).to({y: 0}, 1000).easing(TWEEN.Easing.Elastic.Out).start();
    }
  }
  
  return cardine;
}

function createBumpMesh(geom, imageFile, bumpFile) {
  var texture = THREE.ImageUtils.loadTexture("assets/textures/" + imageFile)
  geom.computeVertexNormals();
  var mat = new THREE.MeshPhongMaterial({side: THREE.DoubleSide});
  mat.map = texture;
  mat.bumpScale = 0.6;
  var bump = THREE.ImageUtils.loadTexture("assets/textures/" + bumpFile);
  mat.bumpMap = bump;


  var mesh = new THREE.Mesh(geom, mat);

  return mesh;
}

function createLamp(){
  var plafonieraGeometry = new THREE.SphereGeometry(2,32,32,Math.PI,Math.PI);
  var plafonieraMaterial = new THREE.MeshPhongMaterial({color: 0xc6c6c6,blending:THREE.AdditiveBlending, shininess: 80, specular: 0xc6c6c6, wireframe: false, side: THREE.DoubleSide, metal:true});

  var plafoniera = new THREE.Mesh(plafonieraGeometry,plafonieraMaterial);
  plafoniera.rotation.x=Math.PI;

  var pointlight = new THREE.PointLight(0xfffa72, 0,25);
  pointlight.castShadow = true;
  pointlight.position.set(0,0,0);


  plafoniera.add(pointlight);
  
  plafoniera.isOn = false;
  plafoniera.interact = function(){
    if(!plafoniera.isOn){
      pointlight.intensity = 2;
      plafoniera.isOn = true;
    }
    else{
      pointlight.intensity = 0;
      plafoniera.isOn = false;
    }

  }

  return plafoniera;
}
