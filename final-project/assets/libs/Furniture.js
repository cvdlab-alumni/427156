 function insertFurniture(scene){
  var loaderSofa = new THREE.OBJLoader();
  loaderSofa.load('assets/models/soderhamn1.obj', function(obj){


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

  var loaderTavolo = new THREE.OBJLoader();
  loaderTavolo.load('assets/models/diningTable.obj', function(obj){
    //global_o = obj;

    var material = [new THREE.MeshPhongMaterial({color: 0x592A0B , side: THREE.DoubleSide, shading: THREE.FlatShading, castShadow:true,receiveShadow:true})];
    material[0].map = THREE.ImageUtils.loadTexture("assets/textures/wood-texture.jpg");
    var tavolo = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, material);
    tavolo.rotation.x = Math.PI*0.5;
    tavolo.scale.set(0.09,0.09,0.11);
    tavolo.position.set(78,40,1);
    scene.add(tavolo);
  });

  var loaderCucina = new THREE.OBJMTLLoader();
  loaderCucina.load('assets/models/cucina.obj','assets/models/cucina.mtl', function(obj){
    //global_o = obj;

    /*var material = [new THREE.MeshLambertMaterial({color: 0xFFF7C2, side: THREE.DoubleSide, shading: THREE.FlatShading, castShadow:true, receiveShadow:true})];
    var cucina = THREE.SceneUtils.createMultiMaterialObject(obj.children[0].geometry, material);
    cucina.rotation.x = Math.PI*0.5;
    //cucina.scale.set(0.09,0.09,0.11);*/
    obj.position.set(10,10,10);
    scene.add(obj);
  });
  return;
}