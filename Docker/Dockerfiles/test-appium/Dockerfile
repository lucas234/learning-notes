FROM ubuntu:19.10
MAINTAINER liulucas
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y curl \
	unzip \
	vim \
	wget \
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
ARG PACKAGE_NAME="sdk-linux-4333796.zip"
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
#RUN mkdir -p ~/.android && \
#    touch ~/.android/repositories.cfg && \
#    echo y | sdkmanager "platform-tools" && \
#    echo y | sdkmanager "build-tools;$ANDROID_BUILD_TOOLS_VERSION" && \
#    echo y | sdkmanager "platforms;$ANDROID_PLATFORM_VERSION"

ENV PATH=$PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools


#===============================
# install appium、appium-doctor
#===============================

ARG APPIUM_VERSION=1.15.1

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
	apt-get -y install nodejs && \
	npm install -g appium@${APPIUM_VERSION} --unsafe-perm=true --allow-root && \
	npm install -g appium-doctor && \
    exit 0 && \
    npm cache clean && \
    apt-get remove --purge -y npm && \
    apt-get autoremove --purge -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get clean
	
EXPOSE 4723

# Clean Up APT when finished
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

























