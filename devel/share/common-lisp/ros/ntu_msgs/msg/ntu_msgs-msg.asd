
(cl:in-package :asdf)

(defsystem "ntu_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "HydrophoneData" :depends-on ("_package_HydrophoneData"))
    (:file "_package_HydrophoneData" :depends-on ("_package"))
  ))