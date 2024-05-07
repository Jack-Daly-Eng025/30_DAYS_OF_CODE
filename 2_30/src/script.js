

/* We don't don't question why it works, we just hope it does */
import * as THREE from "https://cdn.skypack.dev/three@0.148.0"



const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer({
	canvas: document.querySelector('#bg'), 

});
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize( window.innerWidth, window.innerHeight );
camera.position.setZ(30);

document.body.appendChild( renderer.domElement );

/*Play around with geometry a little*/
function randColor (){
	var randomColor = "#000000".replace(/0/g,function(){return (~~(Math.random()*16)).toString(16);});
	return randomColor;

}

var shapecolor = randColor();
const geometry = new  THREE.TorusKnotGeometry(0.99,1.55,12.5,20.5); 
const material = new THREE.MeshBasicMaterial( { color: shapecolor, wireframe: true} );
const tknot = new THREE.Mesh( geometry, material );
scene.add( tknot );


camera.position.z = 5;


function animate() {
	requestAnimationFrame( animate );

	tknot.rotation.x += 0.005;
	tknot.rotation.y += 0.001;
	tknot.rotation.z += 0.005;

	renderer.render( scene, camera );
}

animate();