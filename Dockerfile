# Starting from a minimalist image
FROM ruby:2.7
# Reference for help contact me
LABEL maintainer="chris@adadev.org"

# Create a directory for the app
RUN mkdir /app

# Set the working directory for RUN, ADD and COPY
WORKDIR /app

# Add entire student fork (overwrites previously added files)
ARG SUBMISSION_SUBFOLDER
ADD $SUBMISSION_SUBFOLDER /app


COPY ./Gemfile .
RUN gem install bundler
RUN bundle install

# Overwrite the script and test files
ADD test.sh /app
ADD test /app

RUN chmod +x test.sh
