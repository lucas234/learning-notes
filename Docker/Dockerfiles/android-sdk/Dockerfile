FROM ubuntu:19.10
MAINTAINER liulucas
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y curl \
	unzip \
	vim \
	wget \
	sudo \
	openjdk-8-jdk \
	&& rm -rf /var/lib/apt/lists/* 
	
#=========================
# setting java env
#=========================
ENV JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64"  
ENV	PATH=$PATH:$JAVA_HOME/bin

#=========================
# install android sdk 
#=========================
ARG SDK_VERSION=25.2.3 
ARG PACKAGE_NAME="android-sdk-linux.zip"
ARG ANDROID_BUILD_TOOLS_VERSION=28.0.3
ARG ANDROID_PLATFORM_VERSION="android-28"
ENV ANDROID_HOME=/android-sdk

# offline,had downloaded packages
COPY "${PACKAGE_NAME}" .

RUN mkdir -p "${ANDROID_HOME}" && \
	unzip "${PACKAGE_NAME}" -d "${ANDROID_HOME}" && \
	rm -Rf "${PACKAGE_NAME}"

# online
#RUN mkdir -p "${ANDROID_HOME}" && \
#   wget -q https://dl.google.com/android/repository/tools_r${SDK_VERSION}-linux.zip && \
#	unzip "tools_r${SDK_VERSION}-linux.zip" -d "${ANDROID_HOME}" && \
#	rm -Rf "tools_r${SDK_VERSION}-linux.zip"

ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin

# online download other tools
RUN mkdir -p ~/.android && \
    touch ~/.android/repositories.cfg && \
    echo y | sdkmanager "platform-tools" && \
    echo y | sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION" && \
    echo y | sdkmanager "platforms;$ANDROID_PLATFORM_VERSION"

ENV PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools


























