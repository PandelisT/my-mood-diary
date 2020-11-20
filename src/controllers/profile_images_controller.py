from flask import Blueprint, request, abort, current_app, Response
from flask_jwt_extended import jwt_required
from models.ProfileImage import ProfileImage
from models.User import User
from models.Client import Client
import boto3
from main import db
from pathlib import Path
from flask_jwt_extended import get_jwt_identity


profile_images = Blueprint("profile_images",  __name__, url_prefix="/profile/<int:user_id>/image")


@profile_images.route("/", methods=["POST"])
@jwt_required
def profile_image_create(user_id):
    user_id = get_jwt_identity()
    user = Client.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
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
    new_image.client_id = user.id
    user.profile_image.append(new_image)
    db.session.commit()

    return ("", 201)


@profile_images.route("/", methods=["GET"])
@jwt_required
def profile_image_show(user_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    profile_image = ProfileImage.query.filter_by(id=user_id).first()

    if not profile_image:
        return abort(401, description="Invalid profile image")
    bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])

    filename = profile_image.filename
    print("****************************")
    print(filename)
    file_obj = bucket.Object("profile_images/<User test3@test.com>.JPG").get()

    print(file_obj)

    return Response(
        file_obj["Body"].read(),
        mimetype="image/*",
        headers={"Content-Disposition": "attachment;filename=image"}
    )

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
