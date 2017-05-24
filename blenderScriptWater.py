import bpy

modelName = 'frame'
materialName = 'water'
modelPath = "f:\\animation - PCI25\\"
modelType = ".ply"
imageOutPath = "/blenderImage/"
imageType = ".png"

modelTotal = 5 #File Total
curModelNum = 1

#信息
print("Render Start : ")
print(materialName)

def modelRender(modelNum):
    strModelNum = "%d"%modelNum
    modelFullName = modelName + strModelNum #frame1
    modelFullPath = modelPath + modelFullName + modelType #f:\\animation - PCI25\\frame1.ply
    imageOutFullPath = imageOutPath + modelFullName + imageType #/blenderImage/frame1.png
    #导入
    bpy.ops.import_mesh.ply(filepath = modelFullPath)
    #添加材质
    bpy.data.objects[modelFullName].data.materials.append(bpy.data.materials[materialName])
    #渲染并保存图像
    bpy.data.scenes['Scene'].render.filepath = imageOutFullPath
    bpy.ops.render.render( write_still=True ) 
    #删除
    bpy.ops.object.delete()

if __name__ == "__main__":
    while curModelNum <= modelTotal:
	    print("The currently rendered model num : ", curModelNum)
	    modelRender(curModelNum)
	    curModelNum += 1
    print(" render complete! total: " , modelTotal)
