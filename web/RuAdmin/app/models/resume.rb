class Resume < ApplicationRecord
   mount_uploader :attachment, AttachmentUploader # Tells rails to use this uploader for this model.
   validate :resume_size_validation, :if => "resume?"   # Make sure the owner's name is present. 
   def resume_size_validation
    errors[:resume] << "should be less than 5MB" if resume.size > 2.megabytes
   end
end
