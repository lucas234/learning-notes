FROM ubuntu:16.04
MAINTAINER liulucas
ENV ANDROID_HOME    /android-sdk
ENV JAVA_HOME   /usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV PATH       ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${JAVA_HOME}/bin
ENV SDK_VERSION     25.2.3

# setting java env
RUN apt-get update && \
    apt-get install -y curl \
	unzip \
	vim \
	nodejs \
	npm \
	wget \
	openjdk-8-jdk \
	&& apt-get clean
	
#RUN echo "export JAVA_HOME=$(update-java-alternatives -l | awk '{print $3}')" >> ~/.bashrc
#RUN echo "export PATH=$(update-java-alternatives -l | awk '{print $3}')/bin:$PATH" >> ~/.bashrc

# setting android env
RUN mkdir -p "${ANDROID_HOME}" && \
    wget -q https://dl.google.com/android/repository/tools_r${SDK_VERSION}-linux.zip && \
	unzip "tools_r${SDK_VERSION}-linux.zip" -d "${ANDROID_HOME}" && \
	rm -Rf "tools_r${SDK_VERSION}-linux.zip"

RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager "platform-tools" "build-tools;28.0.3" "platforms;android-28"

# Clean Up APT when finished
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*