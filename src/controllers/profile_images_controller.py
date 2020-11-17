from flask import Blueprint, request, jsonify, abort, current_app, Response
from flask_jwt_extended import jwt_required
from services.auth_service import verify_user
from models.ProfileImage import ProfileImage
from models.Journal import Journal
from models.User import User
from schemas.ProfileImageSchema import profile_image_schema
import boto3
from main import db
from pathlib import Path
from  flask_jwt_extended import get_jwt_identity

profile_images = Blueprint("profile_images",  __name__, url_prefix="/profile/<int:user_id>/image")

@profile_images.route("/", methods=["POST"])
@jwt_required
def profile_image_create(user_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    profile = ProfileImage.query.first()

    if not profile:
        return abort(401, description="Invalid")
    
    if "image" not in request.files:
        return  abort(400, description="No Image")
    
    image = request.files["image"]

    if Path(image.filename).suffix not in [".png", ".jpeg", ".jpg", ".gif", ".JPG"]:
        return abort(400, description="Invalid file type")

    filename = f"{user}{Path(image.filename).suffix}"
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
    key = f"profile_images/{filename}"

    bucket.upload_fileobj(image, key)

    new_image = ProfileImage()
    new_image.filename = filename
    profile.profile_image = new_image
    db.session.commit()
    
    return ("", 201)

# @profile_images.route("/<int:id>", methods=["GET"])
# @jwt_required
# @verify_user
# def profile_image_show(user_id, id):
#     profile_image = ProfileImage.query.filter_by(id=id).first()

#     if not profile_image:
#         return abort(401, description="Invalid profile image")

#     bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
#     filename = profile_image.filename
#     file_obj = bucket.Object(f"profile_images/{filename}").get()

#     print(file_obj)

#     return Response(
#         file_obj["Body"].read(),
#         mimetype="image/*",
#         headers={"Content-Disposition": "attachment;filename=image"}
    # )

# @profile_images.route("/<int:id>", methods=["DELETE"])
# @jwt_required
# @verify_user
# def profile_image_delete(book_id, id, user=None):
#     profile = Profile.query.filter_by(id=profile_id, user_id=user.id).first()

#     if not profile:
#         return abort(401, description="Invalid user")
    
#     if profile.profile_image:
#         bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
#         filename = profile.profile_image.filename

#         bucket.Object(f"profile_images/{filename}").delete()

#         db.session.delete(user.user_image)
#         db.session.commit()

#     return ("", 204)